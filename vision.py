import cv2
import numpy as np
from cscore import CameraServer
from networktables import NetworkTables

from grip import GripPipeline

HORIZONTAL_RES = 2952
VERTICAL_RES = 1944


def extra_process(cnt):
    x, y, w, h = cv2.boundingRect(cnt)

    center_x = x + w / 2
    center_y = y + h / 2

    rect = cv2.minAreaRect(cnt)

    angle = VERTICAL_RES - center_x

    width = rect[1][0]
    height = rect[1][1]

    if width < height:
        angle += 90

    table = NetworkTables.getTable('LiveWindow/Vision')
    table.putNumber('x', center_x)
    table.putNumber('y', center_y)
    table.putNumber('angle', angle)


def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    camera = cs.startAutomaticCapture()
    camera.setResolution(HORIZONTAL_RES, VERTICAL_RES)

    NetworkTables.initialize(server='10.56.54.2')

    pipeline = GripPipeline()

    cvSink = cs.getVideo()

    outputStream = cs.putVideo('Shooter', HORIZONTAL_RES, VERTICAL_RES)

    img = np.zeros(shape=(VERTICAL_RES, HORIZONTAL_RES, 3), dtype=np.uint8)

    while True:

        time, img = cvSink.grabFrame(img)

        if time == 0:
            outputStream.notifyError(cvSink.getError())

            continue

        pipeline.process(img)

        if len(pipeline.find_contours_output) > 0:
            extra_process(max(pipeline.find_contours_output,
                              key=cv2.contourArea))

        outputStream.putFrame(pipeline.find_contours_image)
