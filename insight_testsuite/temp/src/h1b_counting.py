import os
import csv

def top_10_count():
    #input and output path
    inputpath,outputpath = './input','./output'
    try:
        files = os.listdir(inputpath)
    except:
        print('no such file or directory')
    #check if there are multiple files in the input fulder
    assert len(files)==1,'multiple file input, please give only 1 input file'
    
    filepath = os.path.join(inputpath,files[0])
    with open(filepath) as f:
        reader = csv.reader(f,delimiter = ';')
        header = next(reader,None)
        #OccuDict and StateDict stores counting of occupation and state
        OccuDict,StateDict = {},{}
        #headerDict maps header to index
        headerDict = {}
        total_records = 0
        for idx,col in enumerate(header):
            if 'case_status' in col.lower():
                headerDict['status'] = idx
            elif 'worksite_state' in col.lower():
                headerDict['state'] = idx
            elif 'soc_name' in col.lower():
                headerDict['occupation'] = idx
        
        if not headerDict['status'] or not headerDict['state'] or not headerDict['occupation']:
            raise Exception('no such columns found')
        
        #if case is CERTIFIED, increase the occupation and state counter
        for row in reader:
            if row[headerDict['status']] == 'CERTIFIED':
                OccuDict[row[headerDict['occupation']]] = OccuDict.get(row[headerDict['occupation']],0) + 1
                StateDict[row[headerDict['state']]] = StateDict.get(row[headerDict['state']],0) + 1
                total_records += 1
                
    #for output file, create list[tuples]: top_10_occu and top_10_state to store counts, and do sorting
    top_10_occu, top_10_state = [],[]
    
    for k,v in OccuDict.items():
        top_10_occu.append((k,v,v/total_records))
    for k,v in StateDict.items():
        top_10_state.append((k,v,v/total_records))
        
    #sort by count
    top_10_occu.sort(key = lambda x:(-x[1],x[0]))
    top_10_state.sort(key = lambda x:(-x[1],x[0]))
    
    top_10_occu_file = os.path.join(outputpath,'top_10_occupations.txt')
    top_10_states_file = os.path.join(outputpath,'top_10_states.txt')
    
    #write into output files
    with open(top_10_occu_file,'w') as outfile:
        outfile.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
        for i in range(min(10,len(top_10_occu))):
            outfile.write('{};{};{:.1%}\n'.format(top_10_occu[i][0],top_10_occu[i][1],top_10_occu[i][2]))
    with open(top_10_states_file,'w') as outfile:
        outfile.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
        for i in range(min(10,len(top_10_state))):
            outfile.write('{};{};{:.1%}\n'.format(top_10_state[i][0],top_10_state[i][1],top_10_state[i][2]))
                    
    
if __name__=='__main__':
    top_10_count()