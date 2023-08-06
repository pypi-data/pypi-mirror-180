import numpy as np
import os
import glob

import torch
from tepe.data.voc_xml import PascalVocReader


def read_xml(xml_path):
    reader = PascalVocReader(xml_path)
    anno_bboxes = reader.get_bbox()
    bboxes = []
    for anno in anno_bboxes:
        label, box = anno.get('name'), anno.get('bndbox')
        bboxes.append(box)

    return torch.tensor(bboxes)


def box_iou(box1, box2):
    """
    Return intersection-over-union (Jaccard index) of boxes.
    Both sets of boxes are expected to be in (x1, y1, x2, y2) format.
    Arguments:
        box1 (Tensor[N, 4])
        box2 (Tensor[M, 4])
    Returns:
        iou (Tensor[N, M]): the NxM matrix containing the pairwise
            IoU values for every element in boxes1 and boxes2
    """

    def box_area(box):
        # box = 4xn
        return (box[2] - box[0]) * (box[3] - box[1])

    area1 = box_area(box1.T)
    area2 = box_area(box2.T)

    # inter(N,M) = (rb(N,M,2) - lt(N,M,2)).clamp(0).prod(2)
    inter = (torch.min(box1[:, None, 2:], box2[:, 2:]) - torch.max(box1[:, None, :2], box2[:, :2])).clamp(0).prod(2)
    return inter / (area1[:, None] + area2 - inter)  # iou = inter / (area1 + area2 - inter)


def cal_true_positive(gt, pred, iou_thr=0.001):
    num_pred = len(pred)
    num_gt = len(gt)
    p_tp, r_tp = 0, 0
    if num_gt > 0 and num_pred > 0:
        ious = box_iou(gt, pred)  # h: num_gt, w: num_pred
        for iou in ious:  # 对于每个GT
            r_tp += int((iou > iou_thr).sum() > 0)  # 只要有重叠即为检出

        ious = ious.view(num_pred, num_gt)
        for iou in ious:  # 对于每个Pred
            p_tp += int((iou > iou_thr).sum() > 0)  # 只要有重叠即为预测正确
        # x = torch.where((iou >= iou_thr))  # 0: y, 1: x
        # print(x)
        # if len(x) > 0:
        #     x = x[1].numpy()
        #     r_tp = len(np.unique(x))

    return p_tp, r_tp


if __name__ == '__main__':
    pred_dir = '/home/zepei/workspace/ad-tepe/outputs/rd_bjguo_101_1110/bjguo/xml_predict'
    label_idr = '/home/zepei/DATA/lenovo_anomaly/bjguo/ground_truth/bad'

    total_pred, total_gt, total_rtp, total_ptp = 0, 0, 0, 0
    for pred_xml_path in glob.glob(os.path.join(pred_dir, '*.xml')):
        if '22273' in pred_xml_path: # or '32428' in pred_xml_path:

            xml_name = os.path.basename(pred_xml_path)
            label_xml_path = os.path.join(label_idr, xml_name)

            pred = read_xml(pred_xml_path)
            gt = read_xml(label_xml_path)

            num_pred = len(pred)
            num_gt = len(gt)
            p_tp, r_tp = cal_true_positive(gt, pred)

            total_pred += num_pred
            total_gt += num_gt
            total_rtp += r_tp
            total_ptp += p_tp
            print(r_tp, p_tp, num_gt, num_pred)
            print(f'{pred_xml_path}')

    precision = total_ptp / total_pred
    recall = total_rtp / total_gt

    print('精度， 召回：', precision, recall)