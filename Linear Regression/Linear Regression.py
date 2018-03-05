import matplotlib.pyplot as plt
import numpy as np
#plt.use('TkAgg')

#
class linReg:
    def __init__(self, inputfile):
        # reads from input file
        self.file = open(inputfile, "r")

        # converts scientific notation into ints
        np.set_printoptions(suppress=True)

        self.xList = []
        self.yList = []

        # Runs until end of file is reached
        for line in self.file:
            # takes in first line
            self.line = line

            # splits numbers by
            # self.line2 = self.line.split("   ")
            self.line2 = self.line.split("   ")
            # print(self.line2)

            # takes out the newline char in the second value
            self.num2 = self.line2[1].split("\n")
            # x list takes in values of x axis as integers, same for y list
            self.xList.append(int(self.line2[0]))
            self.yList.append(int(self.num2[0]))


        # Normalized values of x and y, range [0,1]
        normalx = self.normalize(self.xList, self.yList)[0]
        normaly = self.normalize(self.xList, self.yList)[1]


        # Runs Batch gradient Descent, first on regular data
        batchex = self.batch_gradientdescent(self.xList, self.yList, .1e-10, .00000000001)
        stochex = self.stochastic_gradientdescent(self.xList, self.yList, .001, .000000001)


        # Stochastic Gradient Descent
        # With Normalized Data
        normbatchex = self.batch_gradientdescent(normalx, normaly, 1e-20, .001)
        normstochex = self.stochastic_gradientdescent(normalx, normaly, .1e-15, .09)

        # prints data to console for w0 and w1
        print("batch W0 is : " + str(batchex[0]))
        print("batch W1 is : " + str(batchex[1]))
        print("stochastic W0 is : " + str(stochex[0]))
        print("stochastic W1 is : " + str(stochex[1]))

        #String Formats for Data Plot
        stw0 = format(batchex[0], '.5f')
        stw1 = format(batchex[1], '.5f')
        bachw0 = format(stochex[0], '.5f')
        bachw1 = format(stochex[1], '.5f')
        stochstring = 'Stochastic\n' + "y = " + str(stw1) + "x + " + str(stw0)
        bachstring = 'Batch\n' + "y = " + str(bachw1) + "x + " + str(bachw0)



        if inputfile == "dataset english.txt":
            plt.title("English Data Set")
        else:
            plt.title("French Data Set")

        # plots the linear regression with the weights w1 and w0
        plt.plot(self.xList, self.yList, '.')
        # Non-Normal Data Plots for both stochastic and batch
        plt.plot([0, 80000], [batchex[1], 80000*batchex[1]+batchex[0]], color='r')
        plt.plot([0, 80000], [stochex[0], 80000*stochex[1] + stochex[0]], color='b')
        plt.annotate(stochstring, xy=(10000, 5000), color='b')
        plt.annotate(bachstring, xy=(50000, 1000), color='r')
        plt.ylabel('Number of As')
        plt.xlabel('Number of Chars')
        plt.show()


        # normal String Formats for Data Plot
        nsw0 = format(normbatchex[0], '.5f')
        nsw1 = format(normbatchex[1], '.5f')
        nbw0 = format(normstochex[0], '.5f')
        nbw1 = format(normstochex[1], '.5f')
        nstochstring = 'Stochastic\n' + "y = " + str(nsw1) + "x + " + str(nsw0)
        nbachstring = 'Batch\n' + "y = " + str(nbw1) + "x + " + str(nbw0)

        # Same plot but for normal data
        normalplot = plt
        if inputfile == "dataset english.txt":
            normalplot.title("Normalized English Data Set")
        else:
            normalplot.title("Normalized French Data Set")
        normalplot.plot(normalx, normaly, '.')
        normalplot.ylabel('Number of As')
        normalplot.xlabel('Number of Chars')
        normalplot.annotate(nstochstring, xy=(.2, .8), color='r')
        normalplot.annotate(nbachstring, xy=(.5, .2), color='g')
        normalplot.plot([0, 1], [normbatchex[0], 1*normbatchex[1]+normbatchex[0]], color='g')
        normalplot.plot([0, 1], [normstochex[0], 1*normstochex[1]+normstochex[0]], color='r')
        normalplot.show()

    # Gradient Descent Function
    def batch_gradientdescent(self, xvals, yvals, error, alpha):
        if xvals[1] > 1:
            w0 = 1
            w1 = 1
        else:
            w0 = .0001
            w1 = .0001

        wx = self.batchsum_fcn(xvals, yvals, w1, w0)
        number = 0
        w1prev = 0

        while abs(w1-w1prev) > error:
            w1prev = w1
            w0 += alpha * wx[0]

            w1 += alpha * wx[1]
            wx = self.batchsum_fcn(xvals, yvals, w1, w0)
            # print(w1-w1prev)
            number += 1
            # print(number)
        return w0, w1

    # Function to determines w0 and w1 to be used with batch Gradient Descent
    # xvals are the x values inputted from file, same for yvals
    # w1 is weight1 and wo is weight 0
    def batchsum_fcn(self, xvals, yvals, w1, w0):
        # weight values, b for batch, and s for stochastic
        bweight0 = 0
        bweight1 = 0

        # total squared error
        sqerror = 0

        # error for x,y set
        error = 0

        # f(x) with weights plugged in
        yhat = 0

        # single squared error
        # se = 0
        lossw1 = 0
        lossw0 = 0

        # flag choose w
        for x in range(0, len(xvals)):

            # calculate f(x) with new weights
            yhat = (w1*xvals[x] + w0)
            # print("W1: " + str(w1) + " W0: " + str(w0))
            # calculate error
            error = yvals[x] - yhat

            lossw0 += (-2)*error
            lossw1 += (-2)*error*xvals[x]
            # se = error**2
            # sqerror += se
            bweight0 += error
            bweight1 += (error * xvals[x])
            # print("Error: " + str(error)  + " X value " + str(xvals[x]))
            # print("w0: " + str(bweight0) + " w1: " + str(bweight1))
            # print("Y: " + str(yvals[x]) + " Y hat: " + str(yhat))


        return bweight0, bweight1, lossw0, lossw1

    # stochastic gradient descent function in order to create weights for
    # linear regression
    def stochastic_gradientdescent(self, xvals, yvals, error, alpha):
        if xvals[1] > 1:
            w0 = 1
            w1 = 1
        else:
            w0 = .0001
            w1 = .0001
        wx = self.stochasticsum_fcn(xvals[0], yvals[0], w1, w0, alpha)


        count = 0
        # converges with 1000 iterations
        for x in range(1000):

            w0 += wx[0]
            w1 += wx[1]

            wx = self.stochasticsum_fcn(xvals[count], yvals[count], w1, w0, alpha)

            if count == len(xvals)-1:
                count = 0
            else:
                count += 1
            # print("w0 and w1" + str(wx[0]) + " " + str(wx[1]))
            # print("Difference: " + str(w1-w1prev))

        return w0, w1


    # Function to determines w0 and w1 to be used with stochastic Gradient Descent
    # xvals are the x values inputted from file, same for yvals
    # w1 is weight1 and wo is weight 0
    def stochasticsum_fcn(self, xval, yval, w1, w0, alpha):
        # weight values, b for batch, and s for stochastic
        sweight0 = w0
        sweight1 = w1

        # total squared error
        sqerror = 0

        # error for x,y set
        error = 0

        # f(x) with weights plugged in
        yhat = 0

        # single squared error
        se = 0

        # flag choose w

        yhat = (w1*xval + w0)
        # print("yhat is: " + str(yhat))
        error = yval - yhat
        se = error**2
        sqerror += se
        sweight0 = alpha*error
        sweight1 = alpha*error*xval

        return sweight0, sweight1

    def normalize(self, xvals, yvals):
        xmin  = min(xvals)
        xmax = max(xvals)
        ymin = min(yvals)
        ymax = max(yvals)

        xratio = 1/(xmax-xmin)
        yratio = 1/(ymax-ymin)

        normalx = []
        normaly = []
        for x in range(0, len(xvals)):
            normalx.append(0 + xratio*(xvals[x]-xmin))
            normaly.append(0 + yratio*(yvals[x]-ymin))
        return normalx, normaly

programFrench = linReg("dataset french.txt")
programEnglish = linReg("dataset english.txt")

# xT = xvals.transpose()
# # wx = self.batchsum_fcn(xvals, yvals, w1, w0)
# sse = 0
# wvector = np.ones(2)
# for x in range(70000):
#     yhat = np.dot(xvals, wvector)
#
#     yerror = yvals - yhat
#     print("CHECK VALUES")
#     gradient = np.dot(xT, yerror)
#     wvector = wvector - alpha * gradient
#     # print(gradient)
#     # check = np.linalg.norm(wvector)
#     # # print(check)
# return wvector