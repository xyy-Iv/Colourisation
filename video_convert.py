import cv2 as cv
import numpy as np

import os, argparse, yaml

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str, default='[VCB-Studio]Hyouka[05][BDRip][720p][x264_aac].mp4', help='Filename of input video')
    parser.add_argument('--input_dir', type=str, default='/home/yuyang/data/Video/Hyouka/', help='Direcotry of input files')
    parser.add_argument('--output_dir', type=str, default='/home/yuyang/data/Video/Converted/', help='Directory of output files')
    parser.add_argument('--out_dim', type=int, nargs=2, default=None, help='Dimensions of output frames (width, height)')
    parser.add_argument('--fps', type=int, default=None, help='Number of fps of output files')

    args = parser.parse_args()
    return args

def color2bw(inputname, inputpath, outputpath, out_dim, fps):
    if inputname.endswith(".mp4"):
        #print(inputpath+inputname)
        cap = cv.VideoCapture(inputpath + inputname)
        width, height = int(cap.get(3)), int(cap.get(4))

        fourcc = cv.VideoWriter_fourcc(*'mp4v')

        if out_dim == None:
            new_width, new_height = width, height
        else:
            new_width, new_height = out_dim

        if fps == None:
            fps = 23.97

        gray_out = cv.VideoWriter(
            outputpath + 'bw_' + inputname,
            fourcc,
            fps,
            (new_width, new_height),
            isColor=False
        )

        # color_out = cv.VideoWriter(
        #     outputpath + 'color_' + inputname,
        #     fourcc,
        #     fps,
        #     (new_width, new_height),
        #     isColor=True
        # )

        #cap = cv.VideoCapture('vtest.avi')

        # while (cap.isOpened()):
        #     ret, frame = cap.read()
        #     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #     cv.imshow('frame', gray)
        #     if cv.waitKey(1) & 0xFF == ord('q'):
        #         break

        while(cap.isOpened()):
            #print(1)
            ret, frame = cap.read()
            if ret == True:
                frame = cv.resize(frame, (new_width, new_height), interpolation = cv.INTER_LINEAR)
                gray = cv.cvtColor(frame, cv.COLOR_BGR2YCrCb)
                frame = np.transpose(np.transpose(gray, (2, 1, 0))[0], (1, 0))
                # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                #print(frame.shape)
                gray_out.write(frame)

                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
                    # end of the video
            else:
                break

        cap.release()
        gray_out.release()


def main():
    args = parse_args()
    if args.filename == '*':
        for filename in os.listdir(args.input_dir):
            color2bw(inputname=filename, inputpath=args.input_dir, outputpath=args.output_dir, out_dim=args.out_dim,
                     fps=args.fps)
    else:
        print(args.filename, args.input_dir, args.output_dir, args.out_dim, args.fps)
        color2bw(inputname=args.filename, inputpath=args.input_dir, outputpath=args.output_dir, out_dim=args.out_dim,
                 fps=args.fps)

    # cleanup
    cv.destroyAllWindows()

    return 0


if __name__ == '__main__':
    main()