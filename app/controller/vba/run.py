import pandas as pd
import numpy as np
import xlrd
import re
import xlwt
import sys
import os

path = sys.argv[1]

def read_excel(path):
    df = pd.read_excel(path, header=None, dtype=str)

    value = df[0]

    approach = []
    movement = []
    flow     = []
    degree   = []
    delay    = []
    los      = []
    queue    = []
    cycle    = []
    movement_loc = 0
    flow_loc     = 0
    degree_loc   = 0
    delay_loc    = 0
    los_loc      = 0
    queue_loc    = 0
    cycle_loc    = 0
    count    = 0
    # Get all need data
    while (count < value.shape[0]):
        movement_t   = []
        flow_t       = []
        degree_t     = []
        delay_t      = []
        los_t        = []
        queue_t      = []
        cycle_t      = []
        if '[' in value[count]:
            p1 = re.compile(r'[\[](.*?)[\]]', re.S)
            title = re.findall(p1, value[count].replace(u'\xa0', u' '))
        if 'Mov ID' in value[count]:
            if 'Turn' in df.iat[count, 1]:
                location = df.loc[count,:]
                for i in range(len(location)):
                    if 'Turn' in df.iat[count, i]:
                        movement_loc = i
                    if 'Demand Flows' in df.iat[count, i]:
                        flow_loc = i
                    if 'Deg. Satn' in df.iat[count, i]:
                        degree_loc = i
                    if 'Average Delay' in df.iat[count, i]:
                        delay_loc = i
                    if 'Level of' in df.iat[count, i]:
                        los_loc = i
                    if 'Back of Queue' in df.iat[count, i]:
                        if df.iat[count+2, i+1] != 'nan':
                            queue_loc = i+1
                        elif df.iat[count+2, i+2] != 'nan':
                            queue_loc = i+2
                        elif df.iat[count+2, i+3] != 'nan':
                            queue_loc = i+3
                        elif df.iat[count+2, i+4] != 'nan':
                            queue_loc = i+4
                    if 'Aver. No.' in df.iat[count, i]:
                        cycle_loc = i
        if 'South:' in value[count] or 'East:' in value[count] or 'North:' in value[count] or 'West:' in value[count]:
            #             for i in range(len(df[]))
            for j in range(10):
                if 'Approach' in value[count+j+1]:
                    break
                move = df.iat[count+j+1, int(movement_loc)]
                if move == 'L2':
                    move = 'Left'
                elif move == 'T1':
                    move = 'Through'
                elif move == 'R2':
                    move = 'Right'
                elif move == 'U':
                    move = 'U-Turn'
                movement_t.append(move)
                flow_t.append(df.iat[count+j+1, flow_loc])
                degree_t.append(df.iat[count+j+1, degree_loc])
                delay_t.append(df.iat[count+j+1, delay_loc])
                los_t.append(df.iat[count+j+1, los_loc])
                queue_t.append(df.iat[count+j+1, queue_loc])
                cycle_t.append(df.iat[count+j+1, cycle_loc])
            movement.append(np.array(movement_t))
            flow.append(np.array(flow_t))
            degree.append(np.array(degree_t))
            delay.append(np.array(delay_t))
            los.append(np.array(los_t))
            queue.append(np.array(queue_t))
            cycle.append(np.array(cycle_t))
            sub_title = value[count].split(':')
            sub_title = sub_title[1].strip(' ') + '(' + sub_title[0] + ')'
#             sub_title = np.repeat(sub_title, j)
            approach.append(sub_title)
            count = count+j
        count = count + 1
    approach = np.array(approach)
    x, y = np.shape(movement)
    movement = np.array(movement).reshape(x*y,)
    flow = np.array(flow).reshape(x*y,)
    flow = np.rint(flow.astype(np.int)*0.95)
    degree = np.array(degree).reshape(x*y,)
    delay = np.array(delay).reshape(x*y,)
    los = np.array(los).reshape(x*y,)
    queue = np.array(queue).reshape(x*y,)
    cycle = np.array(cycle).reshape(x*y,)
#     print(movement_loc,flow_loc,degree_loc,delay_loc,los_loc,queue_loc,cycle_loc)
    return title, approach, movement, flow, degree, delay, los, queue, cycle, x, y

def set_style(height, bold=False):
    style = xlwt.XFStyle()

    font = xlwt.Font()
    font.bold = bold
    font.name = 'Times New Roman'
    font.color_index = 4
    font.height = height

#     borders= xlwt.Borders()
#     borders.left= 6
#     borders.right= 6
#     borders.top= 6
#     borders.bottom= 6

#     pattern = xlwt.Pattern() # Create the Pattern
# #     pattern.pattern = xlwt.Pattern.SOLID_PATTERN
#     pattern.pattern_fore_color = xlwt.Style.colour_map['dark_purple']

    alignment = xlwt.Alignment() # Create Alignment
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER

    style.font = font
#     style.borders = borders
#     style.pattern = pattern
    style.alignment = alignment

    return style

def write_excel(title, approach, movement, flow, degree, delay, los, queue, cycle, merge_cell, path):
    f = xlwt.Workbook() #Create workbook

    # create sheet1
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    row0 = [u'Approach',u'Movement',u'Flow (pcu/h)',u'Degree of Saturation (v/c)',u'Delay (s)',u'LOS',u'Queue (m)',u'No. of Cycles']
    column0 = approach

    sheet1.write(0,0,title)
    #Create first line
    sheet1.row(1).height_mismatch = True
    sheet1.row(1).height = 256*3
    for i in range(0,len(row0)):
        sheet1.write(1,i,row0[i],set_style(220, bold=True))

    #Create first colume and merge y cells
    i, j = 2, 0
    while i <= merge_cell*len(column0) and j < len(column0):
        sheet1.write_merge(i,i+merge_cell-1,0,0,column0[j],set_style(220))
        i += merge_cell
        j += 1

    #Create rest col
    for m in range(len(movement)):
        for n in range(len(row0)-1):
            if n == 0:
                sheet1.write(2+m,1+n,movement[m],set_style(220))
            elif n == 1:
                sheet1.write(2+m,1+n,flow[m],set_style(220))
            elif n == 2:
                sheet1.write(2+m,1+n,degree[m],set_style(220))
            elif n == 3:
                sheet1.write(2+m,1+n,delay[m],set_style(220))
            elif n == 4:
                sheet1.write(2+m,1+n,los[m],set_style(220))
            elif n == 5:
                sheet1.write(2+m,1+n,queue[m],set_style(220))
            elif n == 6:
                sheet1.write(2+m,1+n,cycle[m],set_style(220))

    (filepath,tempfilename) = os.path.split(path)
    (filename,extension) = os.path.splitext(tempfilename)
    save_name = filepath + '/' + filename + '_formatted' + '.xls'

    f.save(save_name) #Save excel
    print(save_name)

if __name__ == "__main__":
    title, approach, movement, flow, degree, delay, los, queue, cycle, x, y = read_excel(path)
    write_excel(title, approach, movement, flow, degree, delay, los, queue, cycle, y, path)
