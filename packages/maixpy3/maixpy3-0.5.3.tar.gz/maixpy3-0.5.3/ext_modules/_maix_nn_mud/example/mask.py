
from time import time
class Mask:
    #mdsc_path
        # V831
    mdsc_path = "/root/mud/v831_yolo_mask.mud"
        #R329
    # mdsc_path = "/root/mud/r329_yolo_mask.mud"

    labels = ["no wear","wear"]
    anchors = [1.19, 1.98, 2.79, 4.59, 4.53, 8.92, 8.06, 5.29, 10.32, 10.65]

    def __init__(self) -> None:

        from maix import nn
        self.model = nn.load(self.mdsc_path)
        from maix.nn import decoder
        self.decoder = decoder.Yolo2(len(self.labels) , self.anchors , net_in_size = (224, 224) ,net_out_size = (7,7))

    def __del__(self):
        del self.model
        del self.decoder

    def cal_fps(self ,start , end):
        one_second = 1
        one_flash = end - start
        fps = one_second / one_flash
        return  fps

    def draw_rectangle_with_title(self ,img, box, disp_str , fps ):
        img.draw_rectangle(box[0], box[1], box[0] + box[2], box[1] + box[3],color=(255, 0, 0), thickness=2)
        img.draw_string(box[0], box[1]+ box[3] ,disp_str, scale=1,color=(0, 0, 255), thickness=1)
        img.draw_string(0, 0 ,'FPS :'+str(fps), scale=2 ,color=(0, 0, 255), thickness=1)

    def process(self,input):
        t =  time()
        out = self.model.forward(input, quantize=1, layout = "hwc")
        boxes, probs = self.decoder.run(out, nms=0.5, threshold=0.6, img_size=(224,224))
        for i, box in enumerate(boxes):
            class_id = probs[i][0]
            prob = probs[i][1][class_id]
            disp_str = "{}:{:.2f}%".format(self.labels[class_id], prob*100)
            fps = self.cal_fps(t, time())
            self.draw_rectangle_with_title(input, box, disp_str, fps)

def main():
    from maix import display, camera
    app = Mask()

    while True:
        img = camera.capture().resize(size=(224, 224))
        app.process(img)
        display.show(img)
main()