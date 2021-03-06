# 100 Days Of ML - LOG

## Day 1 : July 7 , 2018
 
**Today's progress** : Plotter updated, so now it plots all available history labels. Also diving into Progressive GAN so I can start to implement it as a next one.

**Link to work:**   [Commit](https://github.com/Mylittlerapture/GANLib/commit/6b58af27fcd55b3b32efe17219e3cc952a2df2b4)


## Day 2 : July 8 , 2018
 
**Today's progress** : Start working on Progressive GAN implementation. For now I'm going to implement basic idea of growing layers. Other ideas from original paper will be added gradually. 

**Link to work:**   [Commit](https://github.com/Mylittlerapture/GANLib/commit/eb270d9d9f20295f13cefb0f1251ecad30709a2c), [Commit](https://github.com/Mylittlerapture/GANLib/commit/85c44053e3bf3dff5381dd8938318bdd04ea35cf)


## Day 3 : July 9 , 2018
 
**Today's progress** : Progressive GAN is now growing during training. Not sure about overall structure though. Probably will change it later. 

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/54816d45c9b02e308712e765e78dee97b55b4b56)


## Day 4 : July 10 , 2018
 
**Today's progress** : Added template for Adversarial Autoencoder with little twist to it, trying to test some ideas. 

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/77e18eacb2447458bc809a1ac4bf0a733ae05a0f)


## Day 5 : July 11 , 2018
 
**Today's progress** : Today I experimented with domain to domain encoding, with a little bit of success. Because result code end up way different from AAE I split it to different class called DAAE (Domain based Adversarial Autoencoder)

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/eadf7819fd1e309c70e461b30b808c4cf640fc28)


## Day 6 : July 12 , 2018
 
**Today's progress** : Cleaned up DAAE code and eventually improved results a lot by changing a way how discriminator work.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/91139f51cb4fbe45e122df24aa92ea9dc6c394fb)


## Day 7 : July 13 , 2018
 
**Today's progress** : Turns out my DAAE works very similar to DiscoGAN so I renamed it. It a bit sad that this idea far away from new, on the other hand it is a good reminder to spend more time on research. Also made small description for some GANs within source code.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/eb2b06198b3cccde8bd7b7f1625850dc90cf6842), [Commit](https://github.com/Mylittlerapture/GANLib/commit/758ab2e30811ddebf7d2bc223dd2f89e9a135b62)


## Day 8 : July 14 , 2018
 
**Today's progress** : AAE and AAE_test code changed. Unfortunately it's still not working as it supposed to, at least not good enough. Also added descriptions for remaining GANs.  

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/35d9d23250f101b9fb3902b14297f36c3809d309)


## Day 9 : July 15 , 2018
 
**Today's progress** : AAE now working correctly and store some of training history.  

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/a4839920a56b689ad8c6e7864b0ec00c30f7b6b2)


## Day 10 : July 16 , 2018
 
**Today's progress** : Changed a way how stable mode works for GAN and CGAN. Now it actually produce much better results for GAN and roughly the same for CGAN but faster.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/5d4a42bb09972159ddc2ff5bf45664d7752f174a)


## Day 11 : July 17 , 2018
 
**Today's progress** : Update stable mode for Progressive GAN, models moved out of class.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/5ae9a42c6937b834af1ac97be0cac1c710bdb0d3), [Commit](https://github.com/Mylittlerapture/GANLib/commit/4c30d088003219506f1dbea7cd778df77a3e623a)


## Day 12 : July 18 , 2018
 
**Today's progress** : Fixed savings and verbosity mode for every module. Small improvements in ProgGAN.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/52bc82b91e3232e5e85e6c4cdf07649bd8301e15)


## Day 13 : July 19 , 2018
 
**Today's progress** : Changed a way of storing weights and fix metric test in ProgGAN. Added Pixelwise normalization layer to utils and way of using it to ProgGAN_test.py 

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/818bdb9c8a76dd6f4995d043622652a0eba55d25)


## Day 14 : July 20 , 2018
 
**Today's progress** :  Metric test in ProgGAN fixed again. Added MiniBatchStddev layer from ProgGAN paper.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/1e4345c1b6d4b0f4f984943c1ca51651bfeeb601)


## Day 15 : July 21 , 2018
 
**Today's progress** :  Switch MiniBatchStddev code to tensorflow version. Added MiniBatchDiscrimination layer to utils.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/50dadc9f5a851beaa13479fc84db4d518521faf9)


## Day 16 : July 22 , 2018
 
**Today's progress** :  Made a draft version of smooth fading between layers in ProgGAN.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/60782822e1fb326041acb9640f5ba7bcee86820f)


## Day 17 : July 23 , 2018
 
**Today's progress** :  Today I spent time testing ProgGAN on high resolution faces dataset.


## Day 18 : July 24 , 2018
 
**Today's progress** :  Code for MinibatchDiscrimination layer completely changed. Some improvements in ProgGAN. Still testing it on bigger dataset, but results not so good yet. 

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/a1a7b1cb77616f1364d7ff9bf4051bbc0440cb47)


## Day 19 : July 25 , 2018
 
**Today's progress** :  Added rough implementation of improved Wasserstein loss into ProgGAN.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/5bd92f293c7379c1121908e6e1877f8f98f018c2)


## Day 20 : July 26 , 2018
 
**Today's progress** :  Some improvements in ProgGAN. Now it produce more consistent results, but still breaks if model become too big.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/6de25995c0b36f7d65bde13a7dd7a2c8d3e2991f)


## Day 21 : July 27 , 2018
 
**Today's progress** :  Still working on improvements for ProgGAN. For now there are realized most of significant features from the paper.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/f114b3adb330787c19e8431d6a957ce2339d99a9)


## Day 22 : July 28 , 2018
 
**Today's progress** :  After a number of experiments ProgGAN seems to work a bit better, although far from perfect. I guess it is best result that I can get by now.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/05307d588ecc1341b14bb796df6737c8bdb32c78)


## Day 23 : July 29 , 2018
 
**Today's progress** :  Some changes in ProgGAN code to make it more readable and clear.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/e04d2e005b734b5ce10c09210f449de91e860f51)


## Day 24 : July 30 , 2018
 
**Today's progress** :  Complete working on ProgGAN for now.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/d2a0fcb96b15369cae8990383bd07a34cbbe57fe)


## Day 25 : July 31 , 2018
 
**Today's progress** :  Made a template for CramerGAN on which I'm going to work next.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/d7c17ff5e83e495397e0e8bda5d614d15c4663b0)


## Day 26 : June 1 , 2018
 
**Today's progress** :  A bit of work on CramerGAN, just building the understanding of how it works

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/6e8ff2d5282a917840798ad5b1fea8c7c2577e62)


## Day 27 : June 2 , 2018
 
**Today's progress** :  Building CramerGAN.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/b10865ceda5cbea0b08388a79e34f32ab753be77)


## Day 28 : June 3 , 2018
 
**Today's progress** :  Running first tests on CramerGAN and it is kind of works. What is very surprising, because it far from complete.

**Link to work:**  [Commit](https://github.com/Mylittlerapture/GANLib/commit/7a384068efe5dc2353b63a797a9ba259c1debab1)
