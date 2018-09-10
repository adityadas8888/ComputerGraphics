# Das, Aditya.
# axd5763
# 2018-09-08

import sys

class ModelData() :
  def __init__( self, inputFile = None ) :
    self.m_Vertices = []
    self.m_Faces    = []
    self.m_Window   = []
    self.m_Viewport = []

    if inputFile is not None :
      # File name was given.  Read the data from the file.
      self.loadFile( inputFile )

  def loadFile( self, inputFile ) :
    temp=[]
    with open( inputFile, 'r' ) as fp :
        lines = fp.read().replace('\r','').split('\n')
        for (index, line) in enumerate(lines, start = 1):
          line = line.strip()
          if(line!=''and line[0]!='#'):
            each_line = line.split()

            if each_line[0] == 'v':
              try:  
                for i in range(len(each_line)):
                  if(each_line[i]!= 'v'):
                      temp.append(float(each_line[i]))
                if len(temp)==3:
                  self.m_Vertices.append(tuple(temp))
                  temp = []
                else:
                  print("Line "+str(index)+" has a malformed vertex spec.")
                  temp = []
              except:
                    print("Line "+str(index)+" has a malformed vertex spec.")
                    temp = []

            elif each_line[0] == 'f':
              try:  
                for i in range(len(each_line)):
                  if(each_line[i]!= 'f'):
                      temp.append(int(each_line[i])-1)
                if len(temp)==3:
                  self.m_Faces.append(tuple(temp))
                  temp = []
                else:
                  print("Line "+str(index)+" has a malformed face spec.")
                  temp = []
              except:
                    print("Line "+str(index)+" has a malformed face spec.")
                    temp = []

            elif each_line[0] == 'w':
              try:
                for i in range(len(each_line)):
                  if(each_line[i]!= 'w'):
                    temp.append(float(each_line[i]))
                if len(temp) == 4 and len(self.m_Window) > 0 :
                  print("Line "+str(index)+" is a duplicate window spec.")
                  self.m_Window = tuple(temp)  
                  temp = []
                elif  len(temp) == 4 and len(self.m_Window) == 0:
                  self.m_Window = tuple(temp)
                  temp = []  
                else:
                  print("Line "+str(index)+" has a malformed  window spec.")
                  temp = []                     
              except:
                  print("Line "+str(index)+" has a malformed window spec.")
                  temp = []

            elif each_line[0] == 's':
              try:
                for i in range(len(each_line)):
                  if(each_line[i]!= 's'):
                    temp.append(float(each_line[i]))
                if len(temp) == 4 and len(self.m_Viewport) > 0 :
                  print("Line "+str(index)+" is a duplicate viewport spec.")
                  self.m_Viewport = tuple(temp)  
                  temp = []
                elif  len(temp) == 4:
                  self.m_Viewport = tuple(temp)
                  temp = []  
                else:
                  print("Line "+str(index)+" has a malformed  viewport spec.")
                  temp = []                     
              except:
                  print("Line "+str(index)+" has a malformed viewport spec.")
                  temp = []

  def getFaces( self )    : return self.m_Faces
  def getVertices( self ) : return self.m_Vertices
  def getViewport( self ) : return self.m_Viewport
  def getWindow( self )   : return self.m_Window

def _main() :
  # Get the file name to load.
  fName = sys.argv[1]

  # Create a ModelData object to hold the model data from
  # the supplied file name.
  model = ModelData( fName )

  # Now that it's loaded, print out a few statistics about
  # the model data that we just loaded.
  print( "%s: %d vert%s, %d face%s" % (
    fName,
    len( model.getVertices() ), 'ex' if len( model.getVertices() ) == 1 else 'ices',
    len( model.getFaces() ), '' if len( model.getFaces() ) == 1 else 's' ))

  print( 'First 3 vertices:' )
  for v in model.getVertices()[0:3] :
    print( '     ', v )

  print( 'First 3 faces:' )
  for f in model.getFaces()[0:3] :
    print( '     ', f )

  print( 'Window line:', model.getWindow() )
  print( 'Viewport line:', model.getViewport() )

#---------#
if __name__ == '__main__' :
  _main()

#---------#---------#---------#---------#---------#--------#