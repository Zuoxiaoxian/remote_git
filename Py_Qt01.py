"""
In this example , we crete a simple
window in PyQt4.
"""
import sys
from PyQt4 import QtGui


def main():
    app = QtGui.QApplication(sys.argv)

##每一个PyQt4应用都必须创建一个应用(application)对象，
##这个应用对象位于QtGui模块中。其中的sys.argv参数是由命令行参数组成的列表(list)。
##Python脚本也可以从shell中运行，这是我们控制脚本启动的一种方式。
##【这里暂时不理解也没有关系，影响不大，记住要创建application就行】
    
    w = QtGui.QWidget()
##    QtGui.QWidget是PyQt4所有用户接口对象中的基础类库。
##    我们在这里调用了QtGui.QWidget的默认构造函数，这个构造没有父对象。
##    我们把没有父对象的部件(widget)叫做窗口(window)。
##    【这里对于父对象暂时也不需要理解，理解不到也没关系。这句中我们就是创造了一个没有父对象的部件，也就是创建了一个窗口w。】
    w.resize(250,150)
   # 很好理解，resize()方法可以调整部件的大小，我们把它调整成了250px宽，150px高
    w.move(600,500)
    #move()方法将我们的部件移动到了屏幕上坐标为x=300,y=300的地方。【注：屏幕的坐标是以左上角为原点的，横着是x轴，竖着是y轴。】
    w.setWindowTitle('Simple')
    #这里我们设定了部件（其实是个窗口）的标题，标题将在标题栏中显示。
    w.show()
    #show()方法使我们创建的部件能够在屏幕上显示出来。部件先在内存(memory)中被创建，之后再被显示到屏幕上
    sys.exit(app.exec_())
##    在显示了窗口之后，我们进入了程序的主循环，并且开始处理时间。
##    主循环从窗口接收事件并对部件进行处理。如果我们调用exit()函数或者关闭最主要的部件，主循环将终止。
##    这里的sys.exit()调用保证程序完全退出。 
##    值得一提的是exec_()中有一个下划线，为什么呢？因为exec是一个Python关键字，因此加了下划线。

if __name__ == '__main__':
    main()
