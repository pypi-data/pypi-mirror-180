from __future__ import division


from PyQt5.QtGui import QTransform
from PyQt5.QtCore import pyqtSignal, QPointF, Qt
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem, QFrame
import math

from numpy import roll

import cas_gui_2.indicator_rc



class qfi_ADI (QGraphicsView):

    viewUpdate = pyqtSignal()

    def __init__(self,winParent):
        QGraphicsView.__init__(self)

        self.winParent=winParent

        self.viewUpdate.connect(self.update)

        
        self.m_roll = 0
        self.m_pitch = 0
        self.m_yaw = 0

        self.m_faceDeltaX_new = 0
        self.m_faceDeltaX_old = 0
        self.m_faceDeltaY_new = 0
        self.m_faceDeltaY_old = 0

        self.m_originalHeight = 305
        self.m_originalWidth = 245

        self.a = 242.5
        self.b = 2.5
        self.pitchWith = 1435
        self.pitchHeight = 1435
        self.rollHeight = 500
        self.rollWidth = 13

        self.m_originalPixPerDeg = 1.7

        self.m_originalAdiCtr = QPointF( 232.3/2, 232.3/2 )

        self.m_backZ = -30
        self.m_oxZ = -25
        self.m_faceZ = -20
        self.m_ringZ = -10
        self.m_caseZ = 10

        self.setStyleSheet("background: transparent; border: none")
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setInteractive(False)
        self.setEnabled(False)


        self.m_scene = QGraphicsScene(self)
        
        self.setScene(self.m_scene)

        self.init()

        

    def init (self):
        self.m_scaleX = self.width() / self.m_originalWidth
        self.m_scaleY = self.height() / self.m_originalHeight


        self.m_itemBack = QGraphicsSvgItem(":/qfi/pitch.svg")
        self.m_itemBack.setCacheMode (QGraphicsItem.NoCache)
        self.m_itemBack.setZValue( self.m_backZ )
        self.m_itemBack.setTransform(QTransform.fromTranslate(-(self.width()*self.pitchWith/2/self.m_originalWidth),-(self.height()*self.pitchHeight/2/self.m_originalHeight)))
        self.m_itemBack.setTransform( QTransform.fromScale( self.m_scaleX, self.m_scaleY ), True )
        self.m_itemBack.setTransformOriginPoint( QPointF(1680/2,1680/2) )
        self.m_scene.addItem (self.m_itemBack)

        self.m_itemOx = QGraphicsSvgItem(":/qfi/arrows.svg")
        self.m_itemOx.setCacheMode (QGraphicsItem.NoCache)
        self.m_itemOx.setZValue( self.m_oxZ )
        self.m_itemOx.setTransform(QTransform.fromTranslate(-(self.width()/self.m_originalWidth)*117.5,(self.height()/self.m_originalHeight)*(122.5-(17.2527/2))))
        self.m_itemOx.setTransform( QTransform.fromScale( self.m_scaleX, self.m_scaleY ), True )
        self.m_itemOx.setTransformOriginPoint( QPointF(480/2,17.2527/2) )
        self.m_scene.addItem (self.m_itemOx)

        self.m_itemFace = QGraphicsSvgItem(":/qfi/roll_count_bg.svg")
        self.m_itemFace.setCacheMode (QGraphicsItem.NoCache)
        self.m_itemFace.setZValue( self.m_faceZ )
        self.m_itemFace.setTransform(QTransform.fromTranslate(self.width()*self.b/self.m_originalWidth,self.height()*self.a/self.m_originalHeight))
        self.m_itemFace.setTransform( QTransform.fromScale( self.m_scaleX, self.m_scaleY ), True )
        self.m_itemFace.setTransformOriginPoint( self.m_originalAdiCtr )
        self.m_scene.addItem (self.m_itemFace)

        self.m_itemRing = QGraphicsSvgItem(":/qfi/roll_count.svg")
        self.m_itemRing.setCacheMode (QGraphicsItem.NoCache)
        self.m_itemRing.setZValue( self.m_ringZ )
        self.m_itemRing.setTransform(QTransform.fromTranslate(self.width()*self.rollWidth/2/self.m_originalWidth,self.height()*self.rollHeight/2/self.m_originalHeight))
        self.m_itemRing.setTransform( QTransform.fromScale( self.m_scaleX, self.m_scaleY ), True )
        self.m_itemRing.setTransformOriginPoint( QPointF(232.3125/2,232.3125/2) )
        self.m_scene.addItem (self.m_itemRing)
        


        self.m_itemCase = QGraphicsSvgItem(":/qfi/case.svg")
        self.m_itemCase.setCacheMode (QGraphicsItem.NoCache)
        self.m_itemCase.setZValue( self.m_caseZ )
        self.m_itemCase.setTransform( QTransform.fromScale( self.m_scaleX, self.m_scaleY ), True )
        self.m_itemCase.setTransformOriginPoint( self.m_originalAdiCtr )
        self.m_scene.addItem (self.m_itemCase)

        self.centerOn (self.width()/2, self.height()/2)

        self.updateView()

    def reinit(self):
        if (self.m_scene):
            self.m_scene.clear()
            self.init()


    def update(self):
        self.updateView()
        self.m_faceDeltaX_old  = self.m_faceDeltaX_new
        self.m_faceDeltaY_old  = self.m_faceDeltaY_new

    def setYaw (self, yaw):
        while yaw>360:
            yaw-=360
        while yaw<0:
            yaw+=360
        self.m_yaw = yaw

    def setRoll (self, roll):
        while roll>360:
            roll-=360
        while roll<0:
            roll+=360
        self.m_roll = roll


    def setPitch (self, pitch):
        while pitch>360:
            pitch-=360
        while pitch<0:
            pitch+=360
        if pitch>180:
            pitch-=360
        self.m_pitch = pitch*60/25.5

    def resizeEvent (self, event):
        QGraphicsView.resizeEvent (self,event)
        self.reinit()

    def reset (self):
        self.m_itemBack = None
        self.m_itemFace = None
        self.m_itemRing = None
        self.m_itemCase = None

        self.m_roll =  0.0
        self.m_pitch = 0.0
        self.m_yaw = 0.0


    def updateView(self):

        self.m_scaleX = self.width() / self.m_originalWidth
        self.m_scaleY = self.height() / self.m_originalHeight
        
        self.m_itemBack.setRotation(- self.m_roll)
        self.m_itemRing.setRotation(- self.m_yaw)
        self.m_itemOx.setRotation(- self.m_roll)

        roll_rad = math.pi * self.m_roll / 180.0
        delta  = self.m_originalPixPerDeg * self.m_pitch

        self.m_faceDeltaX_new = self.m_scaleX * delta * math.sin( roll_rad )
        self.m_faceDeltaY_new = self.m_scaleY * delta * math.cos( roll_rad )
       
        self.m_itemBack.moveBy( self.m_faceDeltaX_new - self.m_faceDeltaX_old, self.m_faceDeltaY_new - self.m_faceDeltaY_old )
        self.m_scene.update()
