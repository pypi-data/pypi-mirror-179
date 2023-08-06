from .GenericController import  GenericController
from .UtilsController import  UtilsController
from .Connect_db import Connect_db
from datetime import datetime
class TimeLineClusterClass:
    def __init__(self, data_for_time_line_cluster, source_data, source_detail_data) :
        self.app_name = data_for_time_line_cluster["app_name"]
        self.status = True
        self.generic = GenericController.GenericControllerClass(data_for_time_line_cluster)
        self.connect_db_output = Connect_db.ConnectDB(self.generic.data_app_config["output_db"]["host"] , self.generic.data_app_config["output_db"]["database"] , self.generic.data_app_config["output_db"]["user"] ,self.generic.data_app_config["output_db"]["password"])
        self.connect_db_output.connect_to_db(1,1)  # connect db output 
        self.source_data = source_data
        self.source_detail_data = source_detail_data

        self.store_for_time_line_cluster = data_for_time_line_cluster
        # self.data_for_time_line_cluster = data_for_time_line_cluster

        self.pk_report_name = self.generic.data_app_config["report"]["field_pk"]
        self.pk_report_start_date = self.generic.data_app_config["report"]["field_start_date"]

        self.pk_member_name = ""
        if("field_pk" in self.generic.data_app_config["member"]):
            self.pk_member_name = self.generic.data_app_config["member"]["field_pk"]

        self.pk_member_detail_start_date = ""
        if("member_details" in self.generic.data_app_config): 
            if("field_start_date" in self.generic.data_app_config["member_details"]):          
                self.pk_member_detail_start_date = self.generic.data_app_config["member_details"]["field_start_date"]


    def run(self):
        try:
            if(self.generic.data_generic_config == False or self.generic.data_app_config == False):
                self.status = False
                return 
            if(self.status):

                flag_data = UtilsController.getFlagData()
                    
                if(self.connect_db_output.conn == False or self.connect_db_output.conn == None): # connect db output 
                    print("Connect database output")
                    self.connect_db_output.connect_to_db(1,1)

                last_update_source = UtilsController.readFileJson(self.data_for_time_line_cluster["last_update_path"]) # get last update timestamp

                if(last_update_source == False): # Check last update not found or Error readFileJson function ??
                    self.connect_db_output.closeAllConnection("output")
                    self.status = False
                    self.generic.log.text_long += "last update not found or Error readFileJson function."
                    # self.generic.log.genLog(self.generic.log.text_long, "error")
                    return False

                if(type(source_data) == bool): # Check source data not found or error getSourceData function ??
                    self.connect_db_output.closeAllConnection("output")
                    self.status = False
                    self.generic.log.text_long += "Error getSourceData function."
                    # self.generic.log.genLog(self.generic.log.text_long, "error")
                    return False
                    
                source_data_no_detail = []
                if(len(source_data) > 0): # check source data for process
                    last_update_source = source_data.iloc[len(source_data)-1] # store max update timestamp

                    # sort data by pk, start_date
                    for_drop = []
                    for pk in self.generic.data_app_config["report"]["field_pk"]:
                        for_drop.append(pk)
                    for_drop.append(self.generic.data_app_config["report"]["field_start_date"])
                    source_data = source_data.sort_values(for_drop, ascending=[True, True])
                     # end sort data by pk, start_date

                    for_drop = []
                    for pk in self.pk_report_name:
                        for_drop.append(pk)
                    for_drop.append(self.pk_report_start_date)
                    unique_source_data = source_data.drop_duplicates(for_drop) # duplicates source data for process
                    
                    if(self.source_detail_data != "" or self.source_detail_data != None):
                        source_detail_data = self.source_detail_data
                        
                        unique_source_detail_data = source_detail_data.drop_duplicates([self.pk_member_name]) # duplicates source data detail for process

                        if(len(source_data) != len(unique_source_detail_data)): # check source data no detail
                            source_data_no_detail = source_data[~source_data[self.pk_member_name].isin(unique_source_detail_data[self.pk_member_name])]

                    model_report = self.store_for_time_line_cluster["model"]["report"]
                    data_explore_cluster = []
                    for i , source in enumerate(unique_source_data.iloc): # self.pk_report_name, self.pk_report_start_date
                        self.generic.data_app_config = self.store_for_time_line_cluster["data_app_config"]
                        self.generic.log.text_long = "Process start time : " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " "
                        
                        model_summary = self.store_for_time_line_cluster["model"]["summary"]
                        model_summary.summary_date = source[self.pk_report_start_date]

                        flag_data["sql_for_insert_cluster_execute"]["flag_insert_for_summary_details"] = False
                        source_by_create_date = source_data.loc[(source_data[self.pk_report_start_date] == source[self.pk_report_start_date])] # member source 
                        for pk in self.pk_report_name:
                            source_by_create_date = source_by_create_date.loc[(source_by_create_date[pk]  == source[pk])] # member source 

                        if(self.pk_member_detail_start_date != ""):
                            source_detail_by_create_date = source_detail_data.loc[(source_detail_data[self.pk_member_detail_start_date] == source[self.pk_report_start_date])] # member detail source
                            for pk in self.pk_report_name:
                                source_detail_by_create_date = source_detail_by_create_date.loc[(source_detail_by_create_date[pk]  == source[pk])] # member detail source
                        else:
                            source_detail_by_create_date = []

                        data_cluster_representative = self.generic.getClusterRepresentative(self.connect_db_output, self.generic.data_app_config, source) # get cluster
                        data_explore_cluster = self.generic.exploreCluster(self.connect_db_output, source, unique_source_data, i, source_by_create_date, data_cluster_representative, flag_data, self.generic) # check cluster
                        
                        for pk in self.pk_report_name:
                            self.generic.log.text_long += pk + " : " + str(source[pk]) + " "

                        if(self.pk_member_name != ""):
                            self.generic.log.text_long += self.generic.log.convertDf2StringForLog(source_by_create_date, self.pk_member_name) + " "

                        self.generic.handleProcessMember(self.connect_db_output, source, source_by_create_date, source_detail_by_create_date, source_data_no_detail, model_report, model_summary, flag_data, data_cluster_representative, data_explore_cluster, self.generic)
                        
                        self.generic.handleProcessSummary(self.connect_db_output, source, source_by_create_date, source_detail_by_create_date, model_report, model_summary, flag_data, data_cluster_representative, self.generic)

                        data_process_report = self.generic.handleProcessReport(source, model_report, flag_data, data_cluster_representative, self.generic)
                        model_report = data_process_report[0] # data model report
                        flag_data = data_process_report[1] # flag_data
                        
                        if(self.generic.data_app_config["execute_status"] == 1):
                            self.generic.executeSQLForProcess(self.connect_db_output, flag_data, self.generic)
                        else:
                            self.generic.controller_app["report"].executeSQLForProcess(self.generic.controller_app["report"], self.connect_db_output, flag_data, self.generic)
                            
                        self.generic.log.text_long += "Process end time : " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " "
                        
                    UtilsController.writeLastUpdateSurveyJson(self.store_for_time_line_cluster["last_update_path"] , last_update_source['update_timestamp'])
                
                # if(self.update_timestamp_file_edit == 1):
                #     last_update_place = UtilsController.readFileJson(config.ConfigProcess.path_generic_app + "/"+ self.app_name + "/app_max_update_edit.json")
                  

                #     if(len(data_source_place) > 0):
                #         last_update_place = data_source_place.iloc[len(data_source_place)-1]
                #         data_cluster = self.generic.controller_app["report"].getClusterRepresentativeByPlace(self.generic.controller_app["report"], self.connect_db_output, data_source_place, self.generic)
                #         if(len(data_cluster) > 0):
                #             sql_update_by_place = ""
                #             for data in data_cluster.iloc:
                #                 source_by_place = data_source_place.loc[(data_source_place["place_id"]  == data["place_id"])]
                #                 self.generic.log.text_long = "Update place time : " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " representative_id : " + str(data["representative_id"]) + " place_id : " + str(data["place_id"]) + " place_name : " + str(data["place_name"]) + " "
                #                 sql_update_by_place = self.generic.controller_app["report"].genSqlReportUpdateBySourcePlace(self.generic.controller_app["report"], data, source_by_place, self.generic)
                #                 data_execute_for_update = self.generic.controller_app["report"].executeSQLForUpdateBySourcePlace(self.generic.controller_app["report"], self.connect_db_output, sql_update_by_place)
                #                 # self.generic.log.genLog(self.generic.log.text_long, "info")
                #             print("update place !!")
                #             UtilsController.writeLastUpdateSurveyJson(config.ConfigProcess.path_generic_app + "/"+ self.app_name + "/app_max_update_edit.json" , last_update_place['update_timestamp'])

            self.connect_db_output.closeAllConnection("output")
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
            print("Stop !!")
            self.generic.log.text_long += "Oops! An exception has occured : " + str(error) + " Exception TYPE : " + str(type(error))
            # self.generic.log.genLog(self.generic.log.text_long, "error")
            self.status = False
            self.connect_db_output.closeAllConnection("output")
