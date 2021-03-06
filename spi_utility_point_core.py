from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget, QApplication
import sys, os
from spi_utility_point_ui import Ui_SPIUtilityDialogBase
import pandas as pd
from datetime import datetime, timedelta
from glob import glob
import numpy as np
import math
from scipy.stats import gamma

class spiutility(QtWidgets.QMainWindow):
    def __init__(self):
        super(spiutility, self).__init__()

        self.ui = Ui_SPIUtilityDialogBase()
        self.ui.setupUi(self)

        #Event Connections for Page - Data Preparation
        self.ui.pushButton_11.clicked.connect(self.data_prep_get_input_ppt_file)   #Input Precipitaion Data File Browse Button
        self.ui.pushButton_12.clicked.connect(self.data_prep_get_output_dir)   #Output Directory Browse Button
        self.ui.pushButton_13.clicked.connect(self.data_prep_load_data)   #Load Data Button
        self.ui.pushButton.clicked.connect(self.data_prep_generate_composite)   #Generate Composite Button

        #Event Connections for Page - SPI Calculation
        self.ui.pushButton_9.clicked.connect(self.spi_calc_get_comp_file)   #Browser for Monthly Composite File Button
        self.ui.pushButton_10.clicked.connect(self.spi_calc_get_output_dir)   #Browser for Output Folder Button
        self.ui.pushButton_3.clicked.connect(self.spi_calc_generate_spi)   #Generate SPI Button

    def data_prep_get_input_ppt_file(self):
        dlgx = QFileDialog()
        dlgx.setFileMode(QFileDialog.AnyFile)
        dlgx.setNameFilters(["CSV files (*.csv)"])
        #dlgx.setFilter("CSV files (*.csv)")
        
        
        if dlgx.exec_():
            filenames = dlgx.selectedFiles()
            self.ui.lineEdit_10.setText(str(filenames[0]))

    def data_prep_get_output_dir(self):
        dlgx = QFileDialog()
        dlgx.setFileMode(QFileDialog.Directory)
        
        
        if dlgx.exec_():
            filenames = dlgx.selectedFiles()
            self.ui.lineEdit_11.setText(str(filenames[0]))

    def data_prep_load_data(self):
        csvpath = self.ui.lineEdit_10.text()
        outpath = self.ui.lineEdit_11.text()

        error_flag = False
        
        #Read the CSV file
        try:
            checkdf = pd.read_csv(csvpath)

            #Read Outputs to the Log
            if(len(checkdf.columns) > 2):
                self.ui.textEdit_1.append("<font color = green><br />CSV loaded. Total number of Points : <b>{}</b> and total number of rows : <b>{}</b></font>".format(len(checkdf.columns), len(checkdf)))
            else:
                self.ui.textEdit_1.append("<font color = red><br />Input data can not be recognised. Please ensure that the format is as specified in the instructions above.</font>")
                error_flag = True
                     
        except:
            self.ui.textEdit_1.append("<font color = red><br />Input data can not be recognised. Please ensure that the format is as specified in the instructions above.</font>")
            error_flag = True

        
        
        
        #Check for output folder
        if(os.path.exists(outpath) == False):
            self.ui.textEdit_1.append("<font color = red><br />Invalid Output Directory.</font>")
            error_flag = True

        #Continue if there are no errors.
        if(error_flag == False):
            self.ui.pushButton.setEnabled(True)

    def data_prep_generate_composite(self):
        
        self.ui.textEdit_1.append("<font color = blue><br />Generating Monthly Composite...</font>")

        #Disabling other components while the function runs
        self.ui.pushButton_13.setEnabled(False)
        self.ui.pushButton_11.setEnabled(False)
        self.ui.pushButton_12.setEnabled(False)
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_9.setEnabled(False)
        self.ui.pushButton_10.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        
        #Inputs
        csvpath = self.ui.lineEdit_10.text()
        outpath = self.ui.lineEdit_11.text()
        start_date = self.ui.dateEdit.date()
        start_date = datetime(start_date.year(), start_date.month(), start_date.day())
        

        #Read CSV
        df = pd.read_csv(csvpath)

        df['Date'] = [start_date + timedelta(days=x) for x in range(len(df))]
        df['Month'] = [int(x.month) for x in df['Date']]
        df['Year'] = [int(x.year) for x in df['Date']]

        df = df.drop(columns=['Date'])

        final_df = pd.DataFrame()

        #Reset Progressbar
        QApplication.processEvents()
        prog = 0
        prog_inc = 100 / (len(df['Year'].unique())*12)
        self.ui.progressBar_1.setValue(0)
        QApplication.processEvents()

        for y in df['Year'].unique():
            for m in range(1,13):
                mini_df = df[(df['Year'] == y) & (df['Month'] == m)]
                final_df_to_be_appended = pd.DataFrame()
                final_df_to_be_appended['Year'] = [y]
                final_df_to_be_appended['Month'] = [m]
                for x in df.columns[:-2]:
                    final_df_to_be_appended[x] = mini_df[x].sum()
                final_df = pd.concat([final_df, final_df_to_be_appended])

                QApplication.processEvents()
                prog = prog + prog_inc
                self.ui.progressBar_1.setValue(int(prog))
                QApplication.processEvents()

        
        final_df.to_csv(os.path.join(outpath, 'composite.csv'), index = None)

        #Reset Progressbar
        QApplication.processEvents()
        self.ui.progressBar_1.setValue(0)
        QApplication.processEvents()

        self.ui.textEdit_1.append("<font color = green><br />Monthly composite saved at {}</font>".format(os.path.join(outpath, 'composite.csv')))

        self.ui.pushButton_13.setEnabled(True)
        self.ui.pushButton_11.setEnabled(True)
        self.ui.pushButton_12.setEnabled(True)
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_9.setEnabled(True)
        self.ui.pushButton_10.setEnabled(True)
        self.ui.pushButton_3.setEnabled(True)
        self.ui.lineEdit_15.setText(os.path.join(outpath, 'composite.csv'))
        self.ui.lineEdit_16.setText(outpath)
        self.ui.tabWidget.setCurrentIndex(1)
        
    def spi_calc_get_comp_file(self):
        dlgx = QFileDialog()
        dlgx.setFileMode(QFileDialog.AnyFile)
        dlgx.setNameFilters(["CSV files (*.csv)"])
        #dlgx.setFilter("CSV files (*.csv)")
        
        if dlgx.exec_():
            filenames = dlgx.selectedFiles()
            self.ui.lineEdit_15.setText(str(filenames[0]))

    def spi_calc_get_output_dir(self):
        dlgx = QFileDialog()
        dlgx.setFileMode(QFileDialog.Directory)
        if dlgx.exec_():
            filenames = dlgx.selectedFiles()
            self.ui.lineEdit_16.setText(str(filenames[0]))

    def spi_calc_generate_spi(self):

        error_flag = False

        #Get Inputs
        monthly_comp_file = self.ui.lineEdit_15.text()


        try:
            checkdf = pd.read_csv(monthly_comp_file)
            if(checkdf.columns[0] == 'Year' and checkdf.columns[1] == 'Month'):
                error_flag = False
            else:
                self.ui.textEdit_1.append("<font color = red><br />Invalid Monthly Composite File.</font>")
                error_flag = True
        except:
            self.ui.textEdit_1.append("<font color = red><br />Invalid Monthly Composite File. Read Error1</font>")
            error_flag = True

        output_fol = self.ui.lineEdit_16.text()
        if(os.path.exists(output_fol) == False):
            self.ui.textEdit_1.append("<font color = red><br />Invalid Output Folder Path.</font>")
            error_flag = True

        
        try:
            ts = int(self.ui.lineEdit.text())
            if(ts>36):
                self.ui.textEdit_1.append("<font color = red><br />Invalid Time Scale.</font>")
                error_flag = True
            else:
                error_flag = False
        except:
            self.ui.textEdit_1.append("<font color = red><br />Invalid Time Scale.</font>")
            error_flag = True
        
        try:
            acc_period = int(self.ui.lineEdit_2.text())
            if(acc_period>60):
                self.ui.textEdit_1.append("<font color = red><br />Invalid Accumulation Period.</font>")
                error_flag = True
            else:
                error_flag = False
        except:
            self.ui.textEdit_1.append("<font color = red><br />Invalid Accumulation Period.</font>")
            error_flag = True

        stm_x = self.ui.comboBox_11.currentText()
        if(stm_x == 'January'):
            stm = 1
        elif(stm_x == 'February'):
            stm = 2
        elif(stm_x == 'March'):
            stm = 3
        elif(stm_x == 'April'):
            stm = 4
        elif(stm_x == 'May'):
            stm = 5
        elif(stm_x == 'June'):
            stm = 6
        elif(stm_x == 'July'):
            stm = 7
        elif(stm_x == 'August'):
            stm = 8
        elif(stm_x == 'September'):
            stm = 9
        elif(stm_x == 'October'):
            stm = 10
        elif(stm_x == 'November'):
            stm = 11
        elif(stm_x == 'December'):
            stm = 12
        
        enm_x = self.ui.comboBox_12.currentText()
        if(enm_x == 'January'):
            enm = 1
        elif(enm_x == 'February'):
            enm = 2
        elif(enm_x == 'March'):
            enm = 3
        elif(enm_x == 'April'):
            enm = 4
        elif(enm_x == 'May'):
            enm = 5
        elif(enm_x == 'June'):
            enm = 6
        elif(enm_x == 'July'):
            enm = 7
        elif(enm_x == 'August'):
            enm = 8
        elif(enm_x == 'September'):
            enm = 9
        elif(enm_x == 'October'):
            enm = 10
        elif(enm_x == 'November'):
            enm = 11
        elif(enm_x == 'December'):
            enm = 12

        #---------------If there is no error, lets start with SPI calculation----------------------------------
        if(error_flag == False):

            #Disabling other components while the function runs
            self.ui.pushButton_13.setEnabled(False)
            self.ui.pushButton_11.setEnabled(False)
            self.ui.pushButton_12.setEnabled(False)
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton_9.setEnabled(False)
            self.ui.pushButton_10.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)

            self.ui.textEdit_1.append("<font color = blue><br /><b>SPI Calculation Started...</b></font>")

            #------------------------Accumulation---------------------------------------------------------
            self.ui.textEdit_1.append("<font color=blue>Generating accumulation file...</font>")
            
            #Reset Progress Bar
            progval = 0
            perinc = 100.0 / (len(checkdf) - acc_period - 1)
            self.ui.progressBar_1.setValue(progval)

            acc_df = pd.DataFrame()

            for i in range(acc_period-1, len(checkdf)):
                mini_df = checkdf[i - acc_period + 1: i + 1]

                df_to_be_concat = pd.DataFrame()
                df_to_be_concat['Year'] = [checkdf['Year'].values[i]]
                df_to_be_concat['Month'] = [checkdf['Month'].values[i]]
                for cc in mini_df.columns[2:]:
                    df_to_be_concat[cc] = [mini_df[cc].sum()]

                acc_df = pd.concat([acc_df, df_to_be_concat])
                progval = progval + perinc
                self.ui.progressBar_1.setValue(int(progval))

            acc_df.to_csv(os.path.join(output_fol, 'accumulated_{}.csv'.format(acc_period)), index = None)

            #Reset Progress Bar
            progval = 0
            self.ui.progressBar_1.setValue(progval)

            self.ui.textEdit_1.append("<font color=green>Accumulation file saved at {}</font>".format(os.path.join(output_fol, 'accumulated_{}.csv'.format(acc_period))))
            #---------------------------------------------------------------------------------------------

            #--------------------------------------------------------------------------------------------------------------
            #Generating Composites for SPI
            #--------------------------------------------------------------------------------------------------------------

            months = ['01','02','03','04','05','06','07','08','09','10','11','12'] * 2
                
            composite_month_list = []

            if(stm < enm):
                for i in range(stm - 1, enm - ts + 1):
                    composite_month_list.append(months[i:i+ts])
                    is_multiyear = False 
            elif(stm > enm):
                for i in range(stm - 1, 12 + enm - ts + 1):
                    composite_month_list.append(months[i:i+ts])
                    is_multiyear = True
            else:
                composite_month_list.append(months[stm - 1])
                is_multiyear = False

            self.ui.textEdit_1.append("<font color=blue>Generating Composites...</font>")

            #Reset Progress Bar
            progval = 0
            perinc = 100.0 / (len(acc_df['Year'].unique()) * len(composite_month_list))
            self.ui.progressBar_1.setValue(progval)

            comp_df = pd.DataFrame()    #Composite Output Dataframe

            if(os.path.exists(os.path.join(output_fol,'spivals')) == False):
                os.mkdir(os.path.join(output_fol,'spivals'))

            if(os.path.exists(os.path.join(output_fol,'spivals', str(ts))) == False):
                os.mkdir(os.path.join(output_fol,'spivals', str(ts)))
            
            if(os.path.exists(os.path.join(output_fol,'spivals', str(ts), 'composites')) == False):
                os.mkdir(os.path.join(output_fol,'spivals', str(ts), 'composites'))

            for com in composite_month_list:
                comp_df_each_com = pd.DataFrame()
                for y in range(acc_df['Year'].min(), acc_df['Year'].max() + 1):
                    mini_df_for_each_year = pd.DataFrame()
                    curyr = y
                    for c in com:
                        if(is_multiyear and c == '01'):
                            curyr = curyr + 1
                        mini_df_for_each_year = pd.concat([
                                mini_df_for_each_year,
                                acc_df[(acc_df['Year'] == curyr) & (acc_df['Month'] == int(c))]
                            ])
                    
                    comp_df_to_be_concat = pd.DataFrame()
                    comp_df_to_be_concat['Year'] = [y]
                    for cc in acc_df.columns[2:]:
                        comp_df_to_be_concat[cc] = mini_df_for_each_year[cc].sum()
                    
                    comp_df_each_com = pd.concat([comp_df_each_com, comp_df_to_be_concat])

                    progval = progval + perinc
                    self.ui.progressBar_1.setValue(int(progval))

                comp_df_each_com.to_csv(os.path.join(output_fol,'spivals', str(ts), 'composites', 'COMP_{}_{}.csv'.format(com[0], com[-1])),index = None)

            self.ui.textEdit_1.append("<font color=green>Composites generated at {}</font>".format(os.path.join(output_fol,'spivals', str(ts), 'composites')))
            self.ui.progressBar_1.setValue(0)

            #---------------------------------------------------------------------------------------------

            #--------------------------------------------------------------------------------------------------------------
            # SPI Calculation
            #--------------------------------------------------------------------------------------------------------------
            self.ui.textEdit_1.append("<font color=blue>Calculating SPI...</font>")

            #Reset Progress Bar
            progval = 0
            perinc = 100.0 / (len(glob(os.path.join(output_fol,'spivals', str(ts), 'composites', '*.csv'))))
            self.ui.progressBar_1.setValue(progval)

            #Calculate SPI for each composite csv
            comp_files_list = glob(os.path.join(output_fol,'spivals', str(ts), 'composites', '*.csv'))

            for f in comp_files_list:
                spi_df = pd.read_csv(f)

                for c in spi_df.columns[1:]:
                    vals = spi_df[c].values

                    c0 = 2.515517
                    c1 = 0.802583
                    c2 = 0.010328
                    d1 = 1.4327888
                    d2 = 0.189269
                    d3 = 0.001308

                    shapex, loc, scalex = gamma.fit(vals[vals > 0], floc=0)
                    curvale = np.array(gamma.cdf(vals,shapex, scale = scalex))
                    
                    q = len(vals[vals == 0]) / len(vals)
                    
                    curvale = q + ((1-q) * curvale)
                    
                    g_vals = [(np.log(1/(c*c)))**0.5 if c <= 0.5 else (np.log(1/((1-c)*(1-c))))**0.5 for c in curvale]
                    
                    g = np.array(g_vals)
                    
                    spi_vals = (g-((c0 +c1 * g+ c2 *g*g)/(1+d1*g+d2*g*g+d3*g*g*g)))
                    
                    for i in range(len(spi_vals)):
                        if(curvale[i] <= 0.5):
                            spi_vals[i] = -1 * spi_vals[i]


                    spi_df[c] = spi_vals

                export_file_name = "SPI{}".format(os.path.basename(f)[4:])
                spi_df.to_csv(os.path.join(output_fol,'spivals', str(ts),export_file_name), index = None)

                progval = progval + perinc
                self.ui.progressBar_1.setValue(int(progval))
            
            self.ui.textEdit_1.append("<font color=green>Calculates SPI are saved in {}</font>".format(os.path.join(output_fol,'spivals', str(ts))))

            self.ui.progressBar_1.setValue(0)
            self.ui.textEdit_1.append("<hr>")
            self.ui.pushButton_13.setEnabled(True)
            self.ui.pushButton_11.setEnabled(True)
            self.ui.pushButton_12.setEnabled(True)
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_9.setEnabled(True)
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)





        





#Code to initiate and run the App
app = QtWidgets.QApplication([])

window = spiutility()

window.show()

sys.exit(app.exec())