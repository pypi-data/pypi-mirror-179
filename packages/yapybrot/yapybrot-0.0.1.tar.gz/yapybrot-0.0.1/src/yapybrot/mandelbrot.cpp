#include "pybind11/pybind11.h"

#include "xtensor/xmath.hpp"
#include "xtensor/xarray.hpp"
#include "xtensor/xbuilder.hpp"

#define FORCE_IMPORT_ARRAY
#include "xtensor-python/pyarray.hpp"
#include "xtensor-python/pyvectorize.hpp"

#include <iostream>
#include <numeric>
#include <cmath>

namespace py = pybind11;


xt::pyarray<int> _mandelbrot(int width, int height,
                            double xmin, double xmax,
                            double ymin, double ymax,
                            int max_iter,
                            xt::pyarray<int> palette)
{

    xt::pyarray<int> mandel = xt::empty<int>({width, height, 3});
    
    double x, y, x0, y0, x2, y2;
    int iter;
    
    for (int i = 0; i < width; i++) {
        for (int j = 0; j < height; j++) {

            x = 0;
            y = 0;
            x2 = 0;
            y2 = 0;
            x0 = xmin + i * (xmax - xmin) / (width);
            y0 = ymin + j * (ymax - ymin) / (height);
            iter = 0;

            for (int k = 0; k < max_iter; k++) {
                if (x2 + y2 > 4){
                    break;
                }
                y = 2 * x * y + y0;
                x = x2 - y2 + x0;
                x2 = x * x;
                y2 = y * y;
                iter++;
            }

            mandel(i, height - j - 1, 0) = palette(iter % max_iter, 0);
            mandel(i, height - j - 1, 1) = palette(iter % max_iter, 1);
            mandel(i, height - j - 1, 2) = palette(iter % max_iter, 2);
        }
    }
    return mandel;
}

PYBIND11_MODULE(_yapybrot, m)
{
    xt::import_numpy();
    m.def("_mandelbrot", &_mandelbrot, "Plot a Mandelbrot of a given width and height");
}