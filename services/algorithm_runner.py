from app.services.commands.command_invoker import CommandInvoker
from app.services.image_service import ImageService


class AlgorithmRunner:
    def __init__(self, invoker: CommandInvoker, image_service: ImageService):
        self.__invoker = invoker
        self.__image_service = image_service

    def run(self):
        while video.isOpened():
            exists, frame = video.read()
            if not exists:
                video.release()
                detection_timer.stop()
                break

            height, width = frame.shape[:2]

            croped = cv2.bitwise_and(
                frame, frame, mask=(OpeningAndClosing(guass_thresholding)))

            grey = cv2.cvtColor(croped, cv2.COLOR_BGR2GRAY)
            contours, _ = cv2.findContours(
                grey, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)  # CHAIN_APPROX_TC89_L1
            roi = np.zeros((height, width, 3), np.uint8)

            for cnt in contours:
                #cv2.drawContours(frame, cnt, -1, (255, 0, 255), 7)
                approx = cv2.approxPolyDP(
                    cnt, 0.01 * cv2.arcLength(cnt, True), True)
                if (len(approx) >= 4 and cv2.contourArea(cnt) > 10):
                    x, y, w, h = cv2.boundingRect(approx)
                    roi[y:y+h, x:x+w] = frame_c[y:y+h, x:x+w]
                    cnt_c = frame_c[y:y+h, x:x+w].copy()
                    cnt_c = cv2.resize(cnt_c, (224, 224))
                    cnt_c = cnt_c.reshape(1, 224, 224, 3)
                    cnt_c = cnt_c.reshape(-1, 224, 224, 3)
                    pred = model.predict(cnt_c)
                    p = get_label(pred)
                    if(p != 0):
                        cv2.rectangle(frame, (x, y), (x + w, y + h),
                                      (0, 255, 0), 2)
                        cv2.putText(frame, str(p), (x + w + 20, y + 20),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
