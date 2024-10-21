"""medical codes from Ahmed's excel file: ICD code for Ltx and cardiac risk-Final_UTP"""

import pandas as pd
import numpy as np
import csv
import os
import sys
from datetime import datetime
import pickle

import path_jf as pjf
cur_time = datetime.now()
print('Start working at: ', cur_time)

med_codes_path = pjf.med_codes
in_path = pjf.in_path
conf_path = '/raid/jfeng2/code_utp_processing/output/dict/'

"""Liver transplant: codes for cohort selection"""
liver_transplant = {
    'icd_dx_10':['Z48.23','Z94.4','T86.49','T86.40','T86.43'],
    'icd_dx_9':['V42.7','996.82'],
    'cpt':['47133','47135','47140','47141','47142','47143','47144','47145','47146','47147'],
    'icd_px_10':['0FY00Z0'],
    'icd_px_9':['50.5']
    }

## Codes for comordibitis labeling
# conf_ls = ['mi','af','ca','hf','pe','stroke']

# for n in conf_ls: 
#     fn = n
#     label_out_path = os.path.join(conf_path,fn)
#     #os.makedirs(label_out_path)
#     print("Directory '%s' created" %fn)
#     label_out_path = label_out_path+'/'+fn

#     # icd9 
#     icd9_file = fn+'_icd9.txt' 
#     icd9_df = pd.read_csv(med_codes_path+icd9_file, sep="\t")
#     icd9_df.columns = ['diag_cd']
#     print('', icd9_df.head(3))
#     icd9_ls = [str(x) for x in icd9_df.diag_cd]
#     print('\n icd 9 codes to filter for ',fn, ' ',len(icd9_ls))

#     ## icd 10
#     icd10_file = fn+'_icd10.txt' 
#     icd10_df = pd.read_csv(med_codes_path+icd10_file, sep="\t")
#     icd10_df.columns = ['diag_cd']
#     print('', icd10_df.head(3))
#     icd10_ls = [str(x) for x in icd10_df.diag_cd]
#     print('\n icd 10 codes to filter for ',fn, ' ',len(icd10_ls))
#     found_patient = []
#     ## Enter the number of file:
#     n=1
#     for n in range (1,54):
#         filename = 'dx_'+str(n)+'.csv'
#         print('', filename)
#         if n==1:
#             df = pd.read_csv(in_path+filename,
#                 dtype={'patid':np.int64,'diag':object,'icd_flag':np.int64, 'fst_dt':object},
#                 low_memory=False)
#         else:
#             df = pd.read_csv(in_path+filename,
#             names = ['patid','fst_dt','diag','icd_flag'],
#             dtype={'patid':np.int64,'icd_flag':np.int64,'diag':object, 'fst_dt':object},
#             low_memory=False)
    
#         df[fn]=np.where((((df['diag'].isin(icd9_ls)) & 
#                 (df['icd_flag']==9))|
#                 ((df['diag'].isin(icd10_ls))&
#                 (df['icd_flag']==10))), 
#                 1, 0)

#         found_df = df.loc[df[fn]==1]
#         found_pid_ls = found_df['patid'].unique().tolist()
#         found_pid = [int(x) for x in found_pid_ls]
#         found_patient_ls = list(found_pid)

#         found_patient.extend(found_patient_ls)

#         print('\n generated dataframe: ', found_df.head(5))

#         found_df.to_csv(label_out_path+'_'+filename,sep='\t',index=False) # was df

#         print('\n Completed recording from split file: ', n)
#         del found_df
#         del df

#     conf_pid = [int(x) for x in found_patient]
#     conf_set = set(conf_pid)
#     conf_patient_final = list(sorted(conf_set))

#     len_conf_patid= len(conf_patient_final)

#     print('\n found patients with diagnosis of one encounter or more: ', len_conf_patid)

#     with open(label_out_path+'_patient_dx.pickle', 'wb') as handle:
#         pickle.dump(conf_patient_final, handle, protocol=pickle.HIGHEST_PROTOCOL)

# print('\n =====end processing files=======')

# end_time = datetime.now()
# ela_time = end_time - cur_time

# print('\n end working at', end_time, '\n elaspe time is: ', ela_time)