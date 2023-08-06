This package provides the ability to run a random convolution on a given image.

Main functions:

* rand_convolve:
    * Returns a randomly convoluted image given an image path as input.

    * Arguments:

        * image: The image path for the convolution.
        * ksize: The size of the 2 dimensional kernel. The shape of the kernel is: (size, size). (default: 3, must be an odd number.)
        * knum: The number of random kernels to generate and use. (default: 20)
            * int n>0: The number of kernels.
            * -1: Use a new kernel for each pixel.
        * ksign: The signs to be used for the kernels. (default: 0)
            * 0: All kernel values are positive.
            * 1: Kernel signs are randomly mixed between negative and positive.
            * 2: All kernel values are negative.
            
    * Returns:

        * A PIL.Image object of the convoluted image.