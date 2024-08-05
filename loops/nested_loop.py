def insertCarriage(): 
    print('')

def insertHorizontalGridLine(times): 
    print('-' * times)        

def insertVerticalGridLine(): 
    print('|', end='')

def createCell(content = ' '):
    print(content, end='')

def createColumn(columnIndex, verticalGridLines): 
    if(columnIndex == verticalGridLines):
        createCell(' ')
        insertCarriage()
    else: 
        createCell(' ')
        insertVerticalGridLine()

def buildGrid(rows, cols): 
    horizontalGridLines = (rows * 2 - 1) - rows 
    verticalGridLines = (cols * 2 - 1) - cols

    for rowIndex in range(rows): 
        for columnIndex in range(cols): 
            createColumn(columnIndex, verticalGridLines)

        if(rowIndex != horizontalGridLines): 
            insertHorizontalGridLine(cols + verticalGridLines)

buildGrid(rows=20, cols=10)
