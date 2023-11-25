# YOLOX_Automatic-Labeling
## Introduction
The codes have been adapted from Megvii-BaseDetection/YOLOX and can assist with automatic labeling. Follow the steps outlined on the [Megvii-BaseDetection/YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) GitHub page to train or evaluate your model. When evaluating your trained model, the modified YOLOX/tools/demo.py can be used to generate XML annotation files that correspond to the evaluation photos. For detailed instructions, refer to the blog posts linked below. If you find this helpful, don't forget to give us a star on GitHub. Thank you!

## Cite YOLOX 
```latex
 @article{yolox2021,
  title={YOLOX: Exceeding YOLO Series in 2021},
  author={Ge, Zheng and Liu, Songtao and Wang, Feng and Li, Zeming and Sun, Jian},
  journal={arXiv preprint arXiv:2107.08430},
  year={2021}
}
```


## Evaluation
```shell

python3 tools/demo.py image -f exps/example/yolox_voc/yolox_voc_s.py -c /yolox_voc_s/best_ckpt.pth --path /your_path/JPEGImages/ --conf 0.3 --nms 0.5 --tsize 640 --save_result --device gpu

```





