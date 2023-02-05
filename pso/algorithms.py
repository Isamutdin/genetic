from newbase import Array
import random


def psoAlgorithm(swarm, g_best, fitfunc, gen, bitl, swlen, w=0.8, c1=2.05, c2=2.05, update_coef=False):
    for t in range(1, gen+1):
        for i in range(swlen):
            r1 = Array([random.random() for _ in range(bitl)])
            r2 = Array([random.random() for _ in range(bitl)])

            swarm[i].velocity = w*swarm[i].velocity + \
                (c1*r1*(swarm[i].best - swarm[i])) + \
                (c2*r2*(g_best - swarm[i]))



            swarm[i][:] = swarm[i][:] + swarm[i].velocity
            swarm[i].fitness.setValues(fitfunc(swarm[i]))

            if swarm[i].best.update(swarm[i]):
                g_best.update(swarm[i])

        w = ((0.4/(gen**2))*(t-gen)**2 + 0.4) * update_coef
        c1 = ((-3*t)/gen + 3.5) * update_coef
        c2 = ((3*t)/gen + 0.5) * update_coef
    
    return swarm, g_best