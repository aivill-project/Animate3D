# Naver 나를 따라하는 아바타
[[Video](https://tv.naver.com/v/16970573)]
[[pdf](https://deview.kr/data/deview/session/attach/13_%EB%A9%94%ED%83%80%EB%B2%84%EC%8A%A4%20%EC%8B%9C%EB%8C%80%EC%97%90%20%EB%82%98%EB%A7%8C%EC%9D%98%20%EB%B6%80%EC%BA%90%20%EB%A7%8C%EB%93%A4%EA%B8%B0.pdf)
]

## Human Pose Estimation

참고논문
* Vnect: Real-time 3D Human Pose Estimation with a Single RGB Camera (SIGGRAPH 2017)
![](Cap_2022-07-27_14-16-04-417.jpg)
    * pc기반 모델, 큰 모델 사이즈(58.4Mb)
    * 5FPS (200ms) on IPhone X
    * 모바일에서는 부적합한 모델
![](Cap_2022-07-27_14-31-07-546.jpg)

![](Cap_2022-07-27_14-32-27-548.jpg)
    * 파라미터, 모델 크기, FLOPS 등 현저하게 감소시킴
    * 모델을 깎으니 정확도도 같이 내려가는 현상 발생하여 Teacher - Student Learning(Distillation)을 사용하여 정확도를 개선함

* 학습 방법(Training)
![](Cap_2022-07-27_14-34-24-632.jpg)

* Joint 개수
![](Cap_2022-07-27_14-35-18-507.jpg)

* 기존 논문과 파라미터를 줄인 논문과의 차이
![](Cap_2022-07-27_14-36-31-402.jpg)

* Qualitative Results
![](Cap_2022-07-27_14-38-25-419.jpg)

* WACV 2020에 발표
![](Cap_2022-07-27_14-39-04-458.jpg)

[https://arxiv.org/abs/2001.05097](https://arxiv.org/abs/2001.05097)

IEEE Winter Conference on Applications of Computer Vision (WACV) 2020