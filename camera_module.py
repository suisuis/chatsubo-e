from brachiograph import BrachioGraph
from picamera import PiCamera
from linedraw import image_to_json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('name', type=str, help='name of picture')
parser.add_argument('contour', type=int, help='contour value. smaller is detailed and slower')
parser.add_argument('hatch', type=int, help='hatch value. smaller is detailed and slower')

args = parser.parse_args()
bg = BrachioGraph(inner_arm=11, outer_arm=15, servo_1_degree_ms=10, servo_2_degree_ms=10, servo_2_centre=1450, pw_down=1040, pw_up=1020, bounds=[-10.0, 9.0, 2.0, 23.0])

camera = PiCamera()
camera.rotation = 180

img_path = '/home/pi/chatsubo-e/images/{}.jpg'
json_path = '/home/pi/chatsubo-e/images/{}.json'
camera.capture(img_path.format(args.name))

image_to_json(args.name, draw_contours=args.contour, draw_hatch=args.hatch) # smaller values are slower are more detailed
bg.plot_file(json_path.format(args.name), bounds=bg.bounds)