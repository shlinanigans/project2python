

"""
ZetCode PyQt4 

it draws a basic black lines using
a pen style.

Gabriel Zapata && Christpoher N. && Sherelien 

"""

'''
the issues encountered here were that the whole library PyQt4 could not be used
accordingly for our inentions due to issues with all the different OS's used to try ato compile the whole code. 

'''

import sys
import PyQt4
from PyQt4 import QtGui, QtCore


from matplotlib.pyplot import figure, show
import numpy
import six


import os, sys, string, random, struct
import win32api, win32con, win32gui
import urllib2, MultipartPostHandler
import win32clipboard, webbrowser, yaml
import Image, ImageGrab
import yaml


choice = raw.input("Enter which function you would like to run(1 = pen, 2 = zoom, 3 = screenshots and saves")

if choice = 1:
    class Example(QtGui.QWidget):
        
        #this functions single sout specific key points within the object of Example to utlilize those aspects for calculations in the function initUI().
        def __init__(self):
            super(Example, self).__init__()
            
            self.initUI()

        #this function predetermines all the ratios of the geometry of the window to display the area to draw.    
        def initUI(self):      

            self.setGeometry(300, 300, 280, 270)
            self.setWindowTitle('Pen styles')
            self.show()

        #this function initializes qp, which is the gui, and uses functions from the libraries(that arent working) to do most of the calculations in the function.
        def paintEvent(self, e):

            qp = QtGui.QPainter()
            qp.begin(self)
            self.drawLines(qp)
            qp.end()


        #takes in the object qp and self for utilization of the method functions for use to create the actual pen to draw on the image.   
        def drawLines(self, qp):
          
            pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)

            qp.setPen(pen)
            qp.drawLine(20, 40, 250, 40)

            pen.setStyle(QtCore.Qt.DashLine)
            qp.setPen(pen)
            qp.drawLine(20, 80, 250, 80)
                  
            
    def main():
        
        app = QtGui.QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())


    if __name__ == '__main__':
        main()




'''
issues we encountered with being able to process the code correctly to where it
worked appropriately is getting matplotlib to work correctly in response to our 
code in the zooming in and out function
'''


'''
Gabriel Z.
ZOOM IN & OUT functionality!
'''


'''
This portion of the code initializes all the variables within the class to none as 
a starting off point and points to the main method variables of itself.

'''
if choice = 2:
    class ZoomPan:
        def __init__(self):
            self.press = None
            self.cur_xlim = None
            self.cur_ylim = None
            self.x0 = None
            self.y0 = None
            self.x1 = None
            self.y1 = None
            self.xpress = None
            self.ypress = None


    '''
    this function scales all the variables specific for this task.
    It calls specific functions from the libraries imported at the top.
    This is the zoom factory  portion in which it is the main part for zooming
    in and out.
    '''

        def zoom_factory(self, ax, base_scale = 2.):
            def zoom(event):
                cur_xlim = ax.get_xlim()
                cur_ylim = ax.get_ylim()

                xdata = event.xdata # get event x location
                ydata = event.ydata # get event y location

                if event.button == 'down':
                    # deal with zoom in
                    scale_factor = 1 / base_scale
                elif event.button == 'up':
                    # deal with zoom out
                    scale_factor = base_scale
                else:
                    # deal with something that should never happen
                    scale_factor = 1
                    print event.button

                new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
                new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

                relx = (cur_xlim[1] - xdata)/(cur_xlim[1] - cur_xlim[0])
                rely = (cur_ylim[1] - ydata)/(cur_ylim[1] - cur_ylim[0])

                ax.set_xlim([xdata - new_width * (1-relx), xdata + new_width * (relx)])
                ax.set_ylim([ydata - new_height * (1-rely), ydata + new_height * (rely)])
                ax.figure.canvas.draw()

            fig = ax.get_figure() # get the figure of interest
            fig.canvas.mpl_connect('scroll_event', zoom)

            return zoom

        def pan_factory(self, ax):
            def onPress(event):
                if event.inaxes != ax: return
                self.cur_xlim = ax.get_xlim()
                self.cur_ylim = ax.get_ylim()
                self.press = self.x0, self.y0, event.xdata, event.ydata
                self.x0, self.y0, self.xpress, self.ypress = self.press

            def onRelease(event):
                self.press = None
                ax.figure.canvas.draw()

            def onMotion(event):
                if self.press is None: return
                if event.inaxes != ax: return
                dx = event.xdata - self.xpress
                dy = event.ydata - self.ypress
                self.cur_xlim -= dx
                self.cur_ylim -= dy
                ax.set_xlim(self.cur_xlim)
                ax.set_ylim(self.cur_ylim)

                ax.figure.canvas.draw()

            fig = ax.get_figure() # get the figure of interest

            # attach the call back
            fig.canvas.mpl_connect('button_press_event',onPress)
            fig.canvas.mpl_connect('button_release_event',onRelease)
            fig.canvas.mpl_connect('motion_notify_event',onMotion)

            #return the function
            return onMotion


    fig = figure()

    ax = fig.add_subplot(111, xlim=(0,1), ylim=(0,1), autoscale_on=False)

    ax.set_title('Click to zoom')
    x,y,s,c = numpy.random.rand(4,200)
    s *= 200 #this is a pointer for 200.

    ax.scatter(x,y,s,c)
    scale = 1.1
    zp = ZoomPan()
    figZoom = zp.zoom_factory(ax, base_scale = scale)
    figPan = zp.pan_factory(ax)

    show() #this function below actually dispays the zoom campability

#####################################################################

'''
This function is suppose to screenshot the screen
and saves it to desktop. Though the issues encountered here were with the libraries.. once again... and this was a secondary we used instead of the main which
was the pyqt4 because we wanted to try other libraries to see if they would work and this is the second option we came up on in which it 'looked' promising
(though it wasnt).

Christopher C.

'''

#####################################################################

if choice = 3:
    startx, starty = 0, 0
    endx, endy     = 0, 0

    scr_x, scr_y   = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN), win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    scr_w, scr_h   = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN), win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)

    PATH           = os.path.abspath("./") + "\\"
    CONF           = yaml.load(open(PATH +  'local_only', 'r'))

    main_thread_id = win32api.GetCurrentThreadId()

    class MainWindow:
        def __init__(self):
            win32gui.InitCommonControls()
            self.hinst = win32api.GetModuleHandle(None)
        def CreateWindow(self):
            className = self.RegisterClass()
            self.BuildWindow(className)
        def RegisterClass(self):
            className = "Cptr"
            message_map = {
                win32con.WM_DESTROY: self.OnDestroy,
                win32con.WM_LBUTTONDOWN: self.OnStart,
                win32con.WM_LBUTTONUP: self.OnEnd,
                win32con.WM_RBUTTONUP: self.OnCancel,
            }
            wc = win32gui.WNDCLASS()
            wc.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
            wc.lpfnWndProc = message_map
            wc.cbWndExtra = 0
            wc.hCursor = win32gui.LoadCursor(0, win32con.IDC_CROSS)
            wc.hbrBackground = 0
            wc.hIcon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
            wc.lpszClassName = className
            wc.cbWndExtra = win32con.DLGWINDOWEXTRA + struct.calcsize("Pi")
            classAtom = win32gui.RegisterClass(wc)
            return className
        def BuildWindow(self, className):
            style = win32con.WS_EX_TRANSPARENT | win32con.WS_EX_TOOLWINDOW | win32con.WS_EX_TOPMOST | win32con.WS_EX_NOACTIVATE
            self.hwnd = win32gui.CreateWindowEx(style,
                                                className,
                                                "Capture",
                                                win32con.WS_POPUP,
                                                scr_x,
                                                scr_y,
                                                scr_w,
                                                scr_h,
                                                0,
                                                0,
                                                self.hinst,
                                                None)
            win32gui.ShowWindow(self.hwnd, win32con.SW_SHOW)
        def OnDestroy(self, hwnd, message, wparam, lparam):
            return True
        def OnStart(self, hwnd, message, wparam, lparam):
            global startx, starty
            startx, starty = win32gui.GetCursorPos()
            return True
        def OnEnd(self, hwnd, message, wparam, lparam):
            global endx, endy
            endx, endy = win32gui.GetCursorPos()
            win32gui.SetCursor(win32gui.LoadCursor(0, win32con.IDC_WAIT))
            url = Finish()
            if url:
                if CONF['copy_link']:
                    set_clipboard(url)
                if CONF['open_browser'] and not CONF['local_only']:
                    webbrowser.open(url)
            self.CloseWindow()
            return True
        def OnCancel(self, hwnd, message, wparam, lparam):
            self.CloseWindow()
            return True
        def CloseWindow(self):
            win32gui.DestroyWindow(self.hwnd)
            win32api.PostThreadMessage(main_thread_id, win32con.WM_QUIT, 0, 0)

    def Finish():
        global startx, starty, endx, endy

        new_filename   = get_random_filename()
        url            = None

        if startx > endx:
            tempx  = endx
            endx   = startx
            startx = tempx
        if starty > endy:
            tempy  = endy
            endy   = starty
            starty = tempy

        if (endx - startx) is 0 or (endy - starty) is 0: 
            return False

        im   = ImageGrab.grab((startx, starty, endx, endy))#'grabs' all the values in which it changes the pixels coninuously to black essentially to imitate a pen.
        sIm  = open(new_filename, "w+b")

        im.save(sIm, "PNG")
        sIm.seek(0)

        if CONF['local_only'] is True:
            return new_filename
        else:
            params = {'file': sIm}
            opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)
            urllib2.install_opener(opener)
                
            try:
                req = urllib2.Request("http://" + CONF['domain'] + "/?key=" + CONF['key'], params)
            except Exception:
                win32api.MessageBox(w.hwnd, 'No connection', 'Capture: Error', win32con.MB_OK | win32con.MB_ICONERROR)
                return False
            else:
                status   = urllib2.urlopen(req).read().strip()
                sIm.close()

                if "YES" in status:
                    url = status[5:]
                else:
                    win32api.MessageBox(w.hwnd, 'Error while uploading, welp', 'Capture: Error', win32con.MB_OK | win32con.MB_ICONERROR)
                    return False

                return url
            return False

    def set_clipboard(string):
        win32clipboard.OpenClipboard(w.hwnd)
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_TEXT, string)
        win32clipboard.CloseClipboard()

    def random_string(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def get_random_filename():
        if not os.path.exists(PATH + "i"):
            os.mkdir(PATH + "i")
            
        name = PATH + "i\\" + random_string() + ".png"

        try:
            open(name)
        except IOError as e:
            return name
        
        get_random_filename()

    w = MainWindow()

    if __name__ == "__main__":
        w.CreateWindow()
        win32gui.PumpMessages()
