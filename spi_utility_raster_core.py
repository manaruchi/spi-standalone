from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget, QApplication
import sys
from spi_utility_raster_ui import Ui_SPIUtilityDialogBase
from glob import glob
from datetime import datetime, timedelta
import os
from osgeo import gdal, osr
import numpy as np
import math
from scipy.stats import gamma

class spiutility(QtWidgets.QMainWindow):
    def __init__(self):
        super(spiutility, self).__init__()

        self.ui = Ui_SPIUtilityDialogBase()
        self.ui.setupUi(self)

        #Event Connections for Page - Data Preparation
        self.ui.pushButton1.clicked.connect(self.data_prep_get_input_dir)   #Input Precipitaion Data Directory Browse Button
        self.ui.pushButton.clicked.connect(self.data_prep_get_output_dir)   #Output Data Directory Browse Button
        self.ui.pushButton_2.clicked.connect(self.data_prep_check_data)     #Check Data Button
        self.ui.pushButton_4.clicked.connect(self.data_prep_generate_monthly_comp)  #Generate Monthly Composite Button

        #Event Connections for Page - SPI Calculation
        self.ui.pushButton_9.clicked.connect(self.spi_calc_browse_monthly_comp_dir)   #Browse for Monthly Composites Folder Button
        self.ui.pushButton_10.clicked.connect(self.spi_calc_browse_output_dir)   #Browse for Output Folder Button
        self.ui.pushButton_3.clicked.connect(self.spi_calc_generate_spi)   #Generate SPI Button

        #Event Connections for Page - Analysis
        self.ui.pushButton_6.clicked.connect(self.analysis_folder_of_SPI_values)   #Browse for folder of SPI values button
        self.ui.pushButton_7.clicked.connect(self.analysis_output_folder)   #Browse for output folder button
        self.ui.pushButton_5.clicked.connect(self.analysis_classify)   #Classify Button

        
    def data_prep_get_input_dir(self):
        dlgx = QFileDialog()
        dlgx.setFileMode(QFileDialog.Directory)
        if dlgx.exec_():
            filenames = dlgx.selectedFiles()
            self.ui.lineEdit.setText(str(filenames[0]))
            
        fileslistq = glob(str(filenames[0]) + "\*.tif")
        if(len(fileslistq)>0):
            try:
                self.ui.lineEdit_3.setText(fileslistq[0].split('\\')[-1].split('_')[-1].split('.')[0])
                self.ui.lineEdit_4.setText(fileslistq[-1].split('\\')[-1].split('_')[-1].split('.')[0])
            except:
                self.ui.lineEdit_3.setText("")
                self.ui.lineEdit_4.setText("")

    def data_prep_get_output_dir(self):
        dlgx = QFileDialog()
        dlgx.setFileMode(QFileDialog.Directory)
        if dlgx.exec_():
            filenames = dlgx.selectedFiles()
            self.ui.lineEdit_2.setText(str(filenames[0]))

    def data_prep_check_data(self):
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton1.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_9.setEnabled(False)
        self.ui.pushButton_10.setEnabled(False)
        self.ui.pushButton_6.setEnabled(False)
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)
        yearbegin = self.ui.lineEdit_3.text()
        yearend = self.ui.lineEdit_4.text()
        datadir = self.ui.lineEdit.text()
        outputdir = self.ui.lineEdit_2.text()

        if(yearbegin == "" or yearend =="" or datadir == "" or outputdir==""):
            self.ui.textEdit.append("< br/><b><font color = red>Insufficient Data. Check if all the mandatory fields are filled with proper values.</font><b>< br/>")

        else:
            w = QWidget()
            messagee = 'The following parameters are selected. \nInput Directory : ' + str(datadir) + "\nOutput Data Directory : " + str(outputdir) + "\nStart Year : " + str(yearbegin) + "\nEnd Year : " + str(yearend) + '\n\nContine to check Data? '
            reply = QMessageBox.question(w, 'Continue?',messagee, QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                yearbegin = int(yearbegin)
                yearend = int(yearend)
                prog_c = 0.0
                inc_c = 100.0 / (yearend-yearbegin + 1)
                
                erroryear = list()
                errordate = list()
                fileslist = glob(os.path.join(datadir, "*.tif"))
                if(os.path.exists(outputdir)==False):
                    os.mkdir(outputdir)
                #---------Check if Datadir, startyear and endyear are correct----------
                if(fileslist == []):
                    self.ui.textEdit.append("< br/><font color = red>Input precipitation directory not found or the directory has no precipitation data in it.</font>< br/>")
                else:
                    if(yearbegin == 0 or yearend ==0):
                        self.ui.textEdit.append("< br/><font color = red>Start year and End Year values are incorrect.</font>< br/>")
                    else:
                        t1 = datetime.now()
                        self.ui.textEdit.append("< br/><font color = blue><b>Checking Data...</b>< br/>Started on : {}</font>".format(t1))

                        i = yearbegin
                        if(len(fileslist)>=(yearend-yearbegin+1)):
                            
                            while(i<=yearend):
                                filepath = fileslist[i-yearbegin]
                                cur_raster = gdal.Open(filepath)
                                
                                leapornot = 0
                                if(i%4==0):
                                    leapornot = 1
                                    if(i%400==0):
                                        leapornot = 1
                                    elif(i%100==0):
                                        leapornot = 0
                                else:
                                    leapornot = 0
                                
                                if(cur_raster is None):
                                    erroryear.append(str(i) + " : Precipitation data raster is missing")
                                else:
                                    if(leapornot==0):
                                        if(cur_raster.RasterCount!=365):
                                            errordate.append(str(i) + " : Incomplete Data. This raster must contain 365 bands")
                                        Arr = 0
                                        m=0
                                        while(m<365):
                                            band = cur_raster.GetRasterBand(m+1)
                                            Arr = band.ReadAsArray()
                                            if(Arr is None):
                                                self.ui.textEdit.append("Error in Band " + str(m+1) + " in year "+str(i))
                                                
                                            band = 0
                                            m = m + 1
                                        
                                    else:
                                        Arr=0
                                        m=0
                                        while(m<366):
                                            band = cur_raster.GetRasterBand(m+1)
                                            Arr = band.ReadAsArray()
                                            if(Arr is None):
                                                self.ui.textEdit.append("Error in Band " + str(m+1) + " in year "+str(i))
                                                
                                            band = 0
                                            m = m + 1
                                        if(cur_raster.RasterCount!=366):
                                            errordate.append(str(i) + " : Incomplete Data. This raster must contain 366 bands")
                                    
                                        
                                cur_raster = 0
                                QApplication.processEvents()
                                prog_c = prog_c + inc_c
                                
                                self.ui.progressBar.setValue(prog_c)
                                QApplication.processEvents()
                                
                                i = i + 1
                            if(erroryear==[] and errordate==[]):
                                t2 = datetime.now()
                                delta = t2 - t1
                                
                                self.ui.textEdit.append("<br /><font color=green><b>Complete Data Available!!! </b><br />Click on Generate Monthly Composite to generate the monthly precipitation composite from the data provided.<br />Finished on : " + str(t2))
                                hrs = delta.seconds // 3600
                                mins = (delta.seconds - (3600*hrs)) // 60
                                secs = delta.seconds - (3600 * hrs) - (60*mins)
                                self.ui.textEdit.append("Time elapsed : " + str(hrs) + " hours " + str(mins)+ " minutes "+ str(secs) + " seconds")
                                self.ui.pushButton_4.setEnabled(True)
                            else:
                                self.ui.pushButton_4.setEnabled(False)
                                self.ui.textEdit.append("<br /><font color=red><b>Data Missing!!! </b>Please check the data. <br />The following errors are found : ")
                                for xx in erroryear:
                                    self.dlg.textEdit.append(xx)
                                for yy in errordate:
                                    self.dlg.textEdit.append(yy)
                                
                               
                        else:
                            self.ui.pushButton_4.setEnabled(False)
                            self.ui.textEdit.append("<br /><font color=red><b>Data Missing!!! </b>Please check the data. <br />The following errors are found : <br />The range of years is greater than the input precipitation data.")
        
        self.ui.progressBar.setValue(0)
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton1.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_9.setEnabled(True)
        self.ui.pushButton_10.setEnabled(True)
        self.ui.pushButton_6.setEnabled(True)
        self.ui.pushButton_7.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)

    def data_prep_generate_monthly_comp(self):
        #Disable other buttons while the function is running
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton1.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_9.setEnabled(False)
        self.ui.pushButton_10.setEnabled(False)
        self.ui.pushButton_6.setEnabled(False)
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)

        #Get inputs
        yearbegin = self.ui.lineEdit_3.text()
        yearend = self.ui.lineEdit_4.text()
        datadir = self.ui.lineEdit.text()
        outdir_m = self.ui.lineEdit_2.text()
        outdir = os.path.join(outdir_m, "Composite")
        
        #Confirmation Message
        w = QWidget()
        messagee = 'Generate Monthly Composites?'
        reply = QMessageBox.question(w, 'Continue?',messagee, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
        
            if(os.path.exists(outdir)==False):
                os.mkdir(outdir)
            yearbegin = int(yearbegin)
            yearend = int(yearend)
            
            perinc = 100.0 / (((yearend - yearbegin) + 1) * 12)
            progval = 0.0
            t1 = datetime.now()
            self.ui.textEdit.append("<hr><font color=blue><b>Generating Monthly Composites...</b><br />Started on : {}</font>".format(t1))

            for year in range(yearbegin, yearend+1):
                filepath = str(datadir) + "/RF_" + str(year) + ".tif"
                cur_raster = gdal.Open(filepath)

                for month in range(1,13):  
                    #Find DOY range
                    start_doy = (datetime(year,month,1) - datetime(year,1,1)).days + 1
                    end_doy = (datetime(year,month+1,1) - datetime(year,1,1)).days if month < 12 else (datetime(year+1,1,1) - datetime(year,1,1)).days
                    rasterArray = 0

                    for i in range(start_doy, end_doy + 1):
                        band = cur_raster.GetRasterBand(i)
                        rasterArray = rasterArray + band.ReadAsArray()
                    
                    geotransform = cur_raster.GetGeoTransform()
                    originX = geotransform[0]
                    originY = geotransform[3]
                    pixelw = geotransform[1]
                    pixelh = geotransform[5]
                    cols = cur_raster.RasterXSize
                    rows = cur_raster.RasterYSize
                    
                    driver = gdal.GetDriverByName("GTiff")

                    fn = os.path.join(outdir, "RF_{}_{}.tif".format(year, month)) if month > 9 else os.path.join(outdir, "RF_{}_0{}.tif".format(year, month))
                    outRaster = driver.Create(fn, cols,rows, 1 , gdal.GDT_Float32,)
                    outRaster.SetGeoTransform((originX, pixelw, 0, originY, 0, pixelh))
                    outRaster.GetRasterBand(1).WriteArray(rasterArray)
                    outRasterSRS = osr.SpatialReference()
                    outRasterSRS.ImportFromWkt(cur_raster.GetProjectionRef())
                    outRaster.SetProjection(outRasterSRS.ExportToWkt())
                    outRaster.FlushCache()

                    #Update the progressbar
                    QApplication.processEvents() 
                    progval = progval + perinc
                    self.ui.progressBar.setValue(progval)
                    QApplication.processEvents()

            outRaster = 0
            cur_raster = 0
            band = 0
            t2 = datetime.now()
            delta = t2 - t1
            self.ui.textEdit.append("<br /><font color = green><b>Monthly composites generated </b> at <br /> {} <br />Finished on : {}".format(outdir, t2))
            hrs = delta.seconds // 3600
            mins = (delta.seconds - (3600*hrs)) // 60
            secs = delta.seconds - (3600 * hrs) - (60*mins)
            self.ui.textEdit.append("Time elapsed : " + str(hrs) + " hours " + str(mins)+ " minutes "+ str(secs) + " seconds")
            
            self.ui.textEdit.append("<hr><font color=purple><b>Proceed to Generate SPI.</b></font><hr>")
            self.ui.label_6.setText("Data Status : Complete")
            if(os.path.exists(os.path.join(outdir_m, "spivals"))==False):
                os.mkdir(os.path.join(outdir_m, "spivals"))

        self.ui.label_15.setText(datadir)
        self.ui.label_16.setText(outdir_m)
        self.ui.lineEdit_7.setText(str(outdir))
        self.ui.lineEdit_8.setText(str(outdir_m))
        self.ui.label_17.setText(str(yearbegin))
        self.ui.label_18.setText(str(yearend))
        self.ui.pushButton_3.setEnabled(True)
        self.ui.progressBar.setValue(0)
        self.ui.tabWidget.setCurrentIndex(1)
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton1.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_9.setEnabled(True)
        self.ui.pushButton_10.setEnabled(True)
        self.ui.pushButton_6.setEnabled(True)
        self.ui.pushButton_7.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)

    def spi_calc_browse_monthly_comp_dir(self):
        dlgx = QFileDialog()
        dlgx.setFileMode(QFileDialog.Directory)
        if dlgx.exec_():
            filenames = dlgx.selectedFiles()
            self.ui.lineEdit_7.setText(str(filenames[0]))

    def spi_calc_browse_output_dir(self):
        dlgx = QFileDialog()
        dlgx.setFileMode(QFileDialog.Directory)
        if dlgx.exec_():
            filenames = dlgx.selectedFiles()
            self.ui.lineEdit_8.setText(str(filenames[0]))
            
    def spi_calc_generate_spi(self):
        #Disable some of the form controls while this function runs
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton1.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_9.setEnabled(False)
        self.ui.pushButton_10.setEnabled(False)
        self.ui.pushButton_6.setEnabled(False)
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)

        #Get Inputs
        ts = self.ui.comboBox.text()
        acc_period = self.ui.comboBox_6.text()
        stm_x = self.ui.comboBox_2.currentText()
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
        
        enm_x = self.ui.comboBox_3.currentText()
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

        #Error flag------------------------------------------------------------
        is_err = 0
        errorlist = []
        
        
        monthly_comp_fol = self.ui.lineEdit_7.text()
        output_fol = self.ui.lineEdit_8.text()
       
        if(monthly_comp_fol == ""):
            is_err = 1
            errorlist.append("Monthly Composites Folder can not be left blank.")
        
        if(output_fol == ""):
            is_err = 1
            errorlist.append("Output Folder can not be left blank.")
        
        if(os.path.exists(output_fol)==False):
            is_err = 1
            errorlist.append("Output path does not exist.")
        
        flistcheck = glob(os.path.join(monthly_comp_fol, "*.tif"))
        if(len(flistcheck)==0):
            is_err = 1
            errorlist.append("No files found in the input precipitation directory.")

        try:
            ts = int(ts)
        except:
            is_err = 1
            errorlist.append("Time scale needs to be an integer")

        try:
            acc_period = int(acc_period)
        except:
            is_err = 1
            errorlist.append("Accumulation Period needs to be an integer")

        #----------------------------------------------------------------------

        if(is_err==1):
            self.ui.textEdit.append("<font color=red><b>The following errors are found.</b><ul>")
            error_list_contents_html = '<ul>'
            for e in errorlist:
                error_list_contents_html = error_list_contents_html + "<li>{}</li>".format(e)
            error_list_contents_html = error_list_contents_html + '</ul>'
            self.ui.textEdit.append(error_list_contents_html)
            self.ui.pushButton_3.setEnabled(True)
        else:
            w = QWidget()
            messagee = 'The following parameters are selected.' + '\nMonthly Composites Folder : ' + str(monthly_comp_fol) + '\nOutput Folder : ' + str(output_fol) + '\nTimescale : ' + str(self.ui.comboBox.text()) + ' months \nAccumulation Period : ' + str(self.ui.comboBox_6.text()) + " months \nStart month : " + str(self.ui.comboBox_2.currentText()) + "\nEnd month : " + str(self.ui.comboBox_3.currentText()) + '\n\nGenerate SPI for the specified duration? '
            reply = QMessageBox.question(w, 'Continue?',messagee, QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                if(os.path.exists(os.path.join(output_fol, "spivals"))==False):
                    os.mkdir(os.path.join(output_fol, "spivals"))
                if(os.path.exists(os.path.join(output_fol, "spivals", str(ts)))==False):
                    os.mkdir(os.path.join(output_fol, "spivals", str(ts)))
                if(os.path.exists(os.path.join(output_fol, "spivals", str(ts), 'composite'))==False):
                    os.mkdir(os.path.join(output_fol, "spivals", str(ts), 'composite'))
                if(os.path.exists(os.path.join(output_fol, "accumulation"))==False):
                    os.mkdir(os.path.join(output_fol, "accumulation"))
                if(os.path.exists(os.path.join(output_fol, "accumulation", str(acc_period)))==False):
                    os.mkdir(os.path.join(output_fol, "accumulation", str(acc_period)))
                


                yearbegin = int(os.path.basename(flistcheck[0]).split('_')[1])
                yearend = int(os.path.basename(flistcheck[-1]).split('_')[1])

                #Mask Generation
                rasterinit = gdal.Open(flistcheck[0])
                self.ui.textEdit.append("<font color=blue>Mask Generation Started...</font>")

                maskarr = np.array(rasterinit.ReadAsArray())
                maskarr = np.where(maskarr >= 0, 1, 0)

                maskgeotransform = rasterinit.GetGeoTransform()
                maskoriginX = maskgeotransform[0]
                maskoriginY = maskgeotransform[3]
                maskpixelw = maskgeotransform[1]
                maskpixelh = maskgeotransform[5]
                maskdriver = gdal.GetDriverByName("GTiff")
                maskfn = os.path.join(output_fol,'mask.tif')
                maskoutRaster = maskdriver.Create(maskfn, maskarr.shape[1],maskarr.shape[0], 1 , gdal.GDT_Float32,)
                maskoutRaster.SetGeoTransform((maskoriginX, maskpixelw, 0, maskoriginY, 0, maskpixelh))
                maskoutRaster.GetRasterBand(1).WriteArray(maskarr)
                maskoutRasterSRS = osr.SpatialReference()
                maskoutRasterSRS.ImportFromWkt(rasterinit.GetProjectionRef())
                maskoutRaster.SetProjection(maskoutRasterSRS.ExportToWkt())
                maskoutRaster.FlushCache()
                self.ui.textEdit.append("<font color=green>Mask Generated</font>")
                QApplication.processEvents()

                #--------------------------------------------------------------------------------------------------------------
                #Calculating Accumulations
                #--------------------------------------------------------------------------------------------------------------
                self.ui.textEdit.append("<font color=blue>Generating accumulation rasters...</font>")

                #Reset Progress Bar
                progval = 0
                perinc = 100.0 / (len(flistcheck) - acc_period - 1)
                self.ui.progressBar.setValue(progval)

                for i in range(acc_period-1, len(flistcheck)):
                    accarr = 0
                    for f in range(i - acc_period + 1, i + 1):
                        accarr = accarr + np.array(gdal.Open(flistcheck[f]).ReadAsArray())
                    
                    accarr = np.where(maskarr == 1, accarr, -66635)

                    accfn = os.path.join(output_fol,'accumulation',str(acc_period),os.path.basename(flistcheck[i]))
                    outRaster = maskdriver.Create(accfn, accarr.shape[1],accarr.shape[0], 1 , gdal.GDT_Float32,)
                    outRaster.SetGeoTransform((maskoriginX, maskpixelw, 0, maskoriginY, 0, maskpixelh))
                    outRaster.GetRasterBand(1).WriteArray(accarr)
                    outRasterSRS = osr.SpatialReference()
                    outRasterSRS.ImportFromWkt(rasterinit.GetProjectionRef())
                    outRaster.SetProjection(outRasterSRS.ExportToWkt())
                    outRaster.FlushCache()

                    #Update the progress bar
                    QApplication.processEvents() 
                    progval = progval + perinc
                    self.ui.progressBar.setValue(progval)
                    QApplication.processEvents()
                
                #Reset Progress Bar
                progval = 0
                self.ui.progressBar.setValue(progval)
                self.ui.textEdit.append("<font color=green>Accumulation rasters generated.</font>")
                #--------------------------------------------------------------------------------------------------------------

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

                self.ui.textEdit.append("<font color=blue>Generating Composites...</font>")

                #Reset Progress Bar
                progval = 0
                perinc = 100.0 / ((yearend - yearbegin + 1) * len(composite_month_list))
                self.ui.progressBar.setValue(progval)

                for y in range(yearbegin, yearend + 1):
                    for com in composite_month_list:
                        comparr = 0
                        curyr = y
                        for c in com:
                            if(is_multiyear and c == '01'):
                                curyr = curyr + 1
                            if(os.path.exists(os.path.join(output_fol,'accumulation',str(acc_period),"RF_{}_{}.tif".format(curyr,c)))):
                                comparr = comparr + np.array(gdal.Open(os.path.join(output_fol,'accumulation',str(acc_period),"RF_{}_{}.tif".format(curyr,c))).ReadAsArray())

                        comparr = np.where(maskarr == 1, comparr, -66635)

                        compfn = os.path.join(output_fol,'spivals',str(ts),'composite','RF_{}_{}_{}_{}.tif'.format(y, curyr, com[0], com[-1])) if is_multiyear else os.path.join(output_fol,'spivals',str(ts),'composite','RF_{}_{}_{}.tif'.format(y,com[0], com[-1]))
                        outRaster = maskdriver.Create(compfn, accarr.shape[1],accarr.shape[0], 1 , gdal.GDT_Float32,)
                        outRaster.SetGeoTransform((maskoriginX, maskpixelw, 0, maskoriginY, 0, maskpixelh))
                        outRaster.GetRasterBand(1).WriteArray(comparr)
                        outRasterSRS = osr.SpatialReference()
                        outRasterSRS.ImportFromWkt(rasterinit.GetProjectionRef())
                        outRaster.SetProjection(outRasterSRS.ExportToWkt())
                        outRaster.FlushCache()

                        #Update the progress bar
                        QApplication.processEvents() 
                        progval = progval + perinc
                        self.ui.progressBar.setValue(progval)
                        QApplication.processEvents()

                #Reset Progress Bar
                progval = 0
                self.ui.progressBar.setValue(progval)
                self.ui.textEdit.append("<font color=green>Composite rasters generated.</font>")
                #--------------------------------------------------------------------------------------------------------------

                #--------------------------------------------------------------------------------------------------------------
                #SPI Calculation
                #--------------------------------------------------------------------------------------------------------------
                self.ui.textEdit.append("<font color=blue>Calculating SPI...</font>")
                
                composite_files = glob(os.path.join(output_fol,'spivals',str(ts),'composite', '*.tif'))

                bigarray = []
                years_list_for_SPI_output = []

                
                for f in composite_files:
                    bigarray.append(np.array(gdal.Open(f).ReadAsArray()))
                    fname = os.path.basename(f)[2:]
                    years_list_for_SPI_output.append('SPI' + fname)

                bigarray = np.array(bigarray)

                #Reset Progress Bar
                progval = 0
                perinc = 100.0 / (bigarray.shape[1] * bigarray.shape[2])
                self.ui.progressBar.setValue(progval)

                #Core SPI Calculation
                for r in range(bigarray.shape[1]):
                    for c in range(bigarray.shape[2]):

                        vals = bigarray[:,r,c]

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

                        bigarray[:,r,c] = spi_vals

                        #Update the progress bar
                        QApplication.processEvents() 
                        progval = progval + perinc
                        self.ui.progressBar.setValue(progval)
                        QApplication.processEvents()

                #Reset Progress Bar
                progval = 0
                self.ui.progressBar.setValue(progval)
                self.ui.textEdit.append("<font color=green>SPI Calculated.</font>")

                #Export Rasters
                self.ui.textEdit.append("<font color=blue>Exporting Rasters...</font>")
                
                #Reset Progress Bar
                progval = 0
                perinc = 100.0 / (bigarray.shape[0])
                self.ui.progressBar.setValue(progval)

                for z in range(bigarray.shape[0]):

                    spiarr = bigarray[z]
                    spiarr = np.where(maskarr == 1, spiarr, -66635)

                    spifn = os.path.join(output_fol,'spivals',str(ts), '{}.tif'.format(years_list_for_SPI_output[z]))
                    outRaster = maskdriver.Create(spifn, accarr.shape[1],accarr.shape[0], 1 , gdal.GDT_Float32,)
                    outRaster.SetGeoTransform((maskoriginX, maskpixelw, 0, maskoriginY, 0, maskpixelh))
                    outRaster.GetRasterBand(1).WriteArray(spiarr)
                    outRasterSRS = osr.SpatialReference()
                    outRasterSRS.ImportFromWkt(rasterinit.GetProjectionRef())
                    outRaster.SetProjection(outRasterSRS.ExportToWkt())
                    outRaster.FlushCache()

                    #Update the progress bar
                    QApplication.processEvents() 
                    progval = progval + perinc
                    self.ui.progressBar.setValue(progval)
                    QApplication.processEvents()

                #Reset Progress Bar
                progval = 0
                self.ui.progressBar.setValue(progval)
                self.ui.textEdit.append("<font color=green>SPI Rasters Exported to {}.</font><hr>".format(os.path.join(output_fol,'spivals',str(ts), )))
        
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton1.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_9.setEnabled(True)
        self.ui.pushButton_10.setEnabled(True)
        self.ui.pushButton_6.setEnabled(True)
        self.ui.pushButton_7.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)

    def analysis_folder_of_SPI_values(self):
        dlgx = QFileDialog()
        dlgx.setFileMode(QFileDialog.Directory)

        if dlgx.exec_():
            filenames = dlgx.selectedFiles()
            self.ui.lineEdit_5.setText(str(filenames[0]))

        filepath = self.ui.lineEdit_5.text()
        fileslista = glob(os.path.join(filepath, "SPI_*.tif"))
        
        
        if(len(fileslista)==0):
            self.ui.textEdit.append("<font color = red>No supported files found in the directory!!!</font>")
            
        
        else:
            self.ui.comboBox_4.clear()
            self.ui.comboBox_5.clear()
            #first files year count
            yearb = fileslista[0][(len(filepath)+1):]
            yeare = fileslista[len(fileslista)-1][(len(filepath)+1):] 
            yearb = yearb[4:8]
            yeare = yeare[4:8]
            x = int(yearb)
            y = int(yeare)
            while(x<=y):
                self.ui.comboBox_4.addItem(str(x))
                self.ui.comboBox_5.addItem(str(x))
                x = x + 1
            
             
            self.ui.pushButton_5.setEnabled(True)                   

    def analysis_output_folder(self):
        dlgx = QFileDialog()
        dlgx.setFileMode(QFileDialog.Directory)
        
        if dlgx.exec_():
            filenames = dlgx.selectedFiles()
            self.ui.lineEdit_6.setText(str(filenames[0]))

        outpath = self.ui.lineEdit_6.text()
        if(os.path.exists(outpath)==False):
            self.dlg.textEdit.append("<font color=red>Output folder not found.</font>")

    def analysis_classify(self):
        w = QWidget()
        messagee = 'Continue analysis with the provided parameters? '
        reply = QMessageBox.question(w, 'Continue?',messagee, QMessageBox.Yes, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
        
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton1.setEnabled(False)
            self.ui.pushButton_2.setEnabled(False)
            self.ui.pushButton_4.setEnabled(False)
            self.ui.pushButton_9.setEnabled(False)
            self.ui.pushButton_10.setEnabled(False)
            self.ui.pushButton_6.setEnabled(False)
            self.ui.pushButton_7.setEnabled(False)
            self.ui.pushButton_5.setEnabled(False)
            currange = []
            ranges = []
            crows = self.ui.tableWidget.rowCount()
            
            anyerror = 0
            xy = 0
            while(xy<crows):
                currange = []
                namev = self.ui.tableWidget.item(xy, 0)
                lval = self.ui.tableWidget.item(xy, 2)
                hval = self.ui.tableWidget.item(xy, 1)
                if((namev is None) == False):
                    if(float(hval.text())>=float(lval.text())):
                        if(namev.text() != ''):
                            currange.append(float(hval.text()))
                            currange.append(float(lval.text()))
                            currange.append(namev.text())
                            ranges.append(currange)
                        
                    else:
                        
                        self.ui.textEdit.append("<font color = red><b>Error in row : " + str(xy + 1) + " </b>: Upper Limit should be greater than Lower Limit. </font>")
                        anyerror = 1
                xy = xy + 1
                
            if(anyerror ==1):
                self.ui.textEdit.append("<font color = red><b>One or more errors are found. Can not Classify.</font></b>")
            
            else:
                t1 = datetime.now()
                outpath = self.ui.lineEdit_6.text()
                filepath = self.ui.lineEdit_5.text()
                fileslistx = glob(os.path.join(filepath, "*.tif"))
                
                
                
                anals = self.ui.comboBox_4.currentIndex()
                anale = self.ui.comboBox_5.currentIndex()
                
                fileslista = fileslistx[anals:(anale+1)]
                
                progval = 0.0
                proginc = 100.0 / (len(ranges) * 2)
                
                cur_raster = gdal.Open(fileslista[0])
                rows = cur_raster.RasterYSize
                cols = cur_raster.RasterXSize
                
                cur_raster = 0
                
                cat = 0
                while(cat<len(ranges)):
            
                    result = np.zeros((rows,cols))
                    result_cur = np.zeros((rows,cols))
                    a = 0
                    while(a<len(fileslista)):
                        result_cur = np.zeros((rows,cols))
                        cur_raster = gdal.Open(fileslista[a])
                        cur_array1 = cur_raster.ReadAsArray()
                        cur_arr = np.array(cur_array1)
                        
                        rows = cur_raster.RasterYSize
                        cols = cur_raster.RasterXSize
                        r = 0
                        c = 0
                        while(r<rows):
                            c = 0
                            while(c<cols):
                                
                                if((cur_arr[r][c]>=ranges[cat][1]) and (cur_arr[r][c]<=ranges[cat][0])):
                                    
                                    result_cur[r][c] = 1
                                    
                                else:
                                    
                                    result_cur[r][c] = 0
                                        
                                c = c + 1
                            r = r + 1
                        
                        
                        result = result + result_cur
                        
                        
                        cur_raster = 0
                        a = a + 1
                        
                    resultx = np.array(result)
                    prob = resultx / len(fileslista)
                    #result = np.where(result>=0, result, None)
                    
                    cur_raster = gdal.Open(fileslista[0])
                    geotransform = cur_raster.GetGeoTransform()
                    originX = geotransform[0]
                    originY = geotransform[3]
                    pixelw = geotransform[1]
                    pixelh = geotransform[5]
                    
                    driver = gdal.GetDriverByName("GTiff")
                    fn = os.path.join(outpath, "c_{}.tif".format(ranges[cat][2]))
                    outRaster = driver.Create(fn, cols,rows, 1 , gdal.GDT_Float32,)
                    outRaster.SetGeoTransform((originX, pixelw, 0, originY, 0, pixelh))
                    outRaster.GetRasterBand(1).WriteArray(result)
                    outRasterSRS = osr.SpatialReference()
                    outRasterSRS.ImportFromWkt(cur_raster.GetProjectionRef())
                    outRaster.SetProjection(outRasterSRS.ExportToWkt())
                    outRaster.FlushCache()
                    outRaster = 0
                    cur_raster = 0
                    self.ui.textEdit.append("<font color = green><b>Count file </b>" + str(fn) + " Generated.</font>")
                    
                    progval = progval + proginc
                    self.ui.progressBar.setValue(progval)
                    QApplication.processEvents()
                    
                    cur_raster = gdal.Open(fileslista[0])
                    geotransform = cur_raster.GetGeoTransform()
                    originX = geotransform[0]
                    originY = geotransform[3]
                    pixelw = geotransform[1]
                    pixelh = geotransform[5]
                    
                    driver = gdal.GetDriverByName("GTiff")
                    fn = os.path.join(outpath + "/p_{}.tif".format(ranges[cat][2]))
                    outRaster = driver.Create(fn, cols,rows, 1 , gdal.GDT_Float32,)
                    outRaster.SetGeoTransform((originX, pixelw, 0, originY, 0, pixelh))
                    outRaster.GetRasterBand(1).WriteArray(prob)
                    outRasterSRS = osr.SpatialReference()
                    outRasterSRS.ImportFromWkt(cur_raster.GetProjectionRef())
                    outRaster.SetProjection(outRasterSRS.ExportToWkt())
                    outRaster.FlushCache()
                    outRaster = 0
                    cur_raster = 0
                    self.ui.textEdit.append("<font color = green><b>Probability file </b>" + str(fn) + " Generated.</font>")
                    
                    progval = progval + proginc
                    self.ui.progressBar.setValue(progval)
                    QApplication.processEvents()
                    cat = cat + 1
                
                t2 = datetime.now()
                delta = t2 - t1
                hrs = delta.seconds // 3600
                mins = (delta.seconds - (3600*hrs)) // 60
                secs = delta.seconds - (3600 * hrs) - (60*mins)
                self.ui.textEdit.append("Time elapsed : " + str(hrs) + " hours " + str(mins)+ " minutes "+ str(secs) + " seconds")
            
                self.ui.progressBar.setValue(0)
                QApplication.processEvents()
                self.ui.pushButton_3.setEnabled(True)
                self.ui.pushButton.setEnabled(True)
                self.ui.pushButton1.setEnabled(True)
                self.ui.pushButton_2.setEnabled(True)
                self.ui.pushButton_4.setEnabled(False)
                self.ui.pushButton_9.setEnabled(True)
                self.ui.pushButton_10.setEnabled(True)
                self.ui.pushButton_6.setEnabled(True)
                self.ui.pushButton_7.setEnabled(True)
                self.ui.pushButton_5.setEnabled(True)    

#Code to initiate and run the App
app = QtWidgets.QApplication([])

window = spiutility()

window.show()

sys.exit(app.exec())