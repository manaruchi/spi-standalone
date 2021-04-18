from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget, QApplication
import sys
from spi_utility_raster_ui import Ui_SPIUtilityDialogBase
from glob import glob
from datetime import datetime, timedelta
import os
from osgeo import gdal, osr

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
                fileslist = glob(datadir + "/*.tif")
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
        self.ui.pushButton_4.setEnabled(True)
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

                    fn = os.path.join(outdir, "RF_{}_{}.tif".format(year, month))
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

            

#Code to initiate and run the App
app = QtWidgets.QApplication([])

window = spiutility()

window.show()

sys.exit(app.exec())