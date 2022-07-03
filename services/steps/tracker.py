from matplotlib.patches import Polygon


class TrackingService:
    def __init__(self, coverage_threshold):
        self.coverage_threshold = coverage_threshold
        self.trackers = []
        self.curr_results = []

    def __calculate_iou(box_1, box_2):
        poly_1 = Polygon(box_1)
        poly_2 = Polygon(box_2)
        iou = poly_1.intersection(poly_2).area / poly_1.union(poly_2).area
        return iou

    def append_tracker(self, tracker):
        self.trackers.append(tracker)

    def update_trackers(self, frame):
        self.curr_results = [t.update(frame) for t in self.trackers if self.is_frame_already_tracked(frame)]

    def is_frame_already_tracked(self, bbox_frame):
        coverage = [self.__calculate_iou(bbox, bbox_frame)
                    for bbox, ok in self.curr_results]
        max_coverage = max(coverage)

        return (max_coverage*100) >= self.coverage_threshold
