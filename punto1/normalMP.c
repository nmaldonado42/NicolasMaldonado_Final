#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include <time.h>
#include<omp.h>

int main(int argc, char ** argv)
{
    #pragma omp parallel
    {
        int thread_id = omp_get_thread_num();
        char file_name[12];
        sprintf(file_name, "dist_%d.txt", thread_id);
        
        FILE *f = fopen(file_name, "w");
        if(f == NULL)
        {
            printf("Error opening file!\n");
            exit(1);
        }
        
        srand48(thread_id);
        int N = 999;
        float x = 0.0;
        fprintf(f, "%f,", x);
        int i;
        for(i = 0; i < N; i++)
        {
            float temp = drand48() * 2 - 1;
            float prop = x + temp;
            float propdf = 0.3989422804014327 * exp(-0.5*prop*prop);
            float xdf = 0.3989422804014327 * exp(-0.5*x*x);
            float test = 1.0;
            if(propdf/xdf < 1.0)
            {
                test = propdf/xdf;
            }
            float u = drand48();
            if(u < test)
            {
                x = prop;
            }
            fprintf(f, "%f,", x);
        }
  }
  return 0;
}