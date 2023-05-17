from PIL import Image
from dtype import METADATA
import numpy as np
import regex as re

class Input_Formatting():
    def __init__(self,
                 query:dict):
        
        self.param_type = {"content_type":"str"}
        self.datatype = "BYTES"
        self.pipeline = query["hf_pipeline"]
        self.input = query["inputs"]
        self.parameters = query.get("parameters")
        
        self.pipeline_dict = dict(  text=["feature-extraction","text-classification","token-classification","fill-mask","summarization","translation","text2text-generation","text-generation"],
                                    image=["image-classification","image-segmentation","object-detection"],
                                    input_param=["question-answering","zero-shot-classification"],
                                    # audio=["audio-classification","automatic-speech-recognition"],
                                    # hg_jsonlist=["table-question-answering","visual-question-answering"],
                                    # coversational=["conversational"]
                                )

    # Pipeline Type
    def pipeline_type(self):
        for type in self.pipeline_dict:
            if self.pipeline in self.pipeline_dict[type]:
                return type

    # Input METADATA Structure
    def input_skeletal(self):
        self.format = dict(METADATA[self.pipeline])
        self.input_format = self.format['inputs']
        return self.input_format

    # Simplifying Input
    def query_formatting(self,input):
        # Single Input
        if isinstance(input,str):
            return [input]

        # List of Inputs
        elif isinstance(input,list):
            return input
        
        # Dict of Input
        elif isinstance(input,dict):
            converted = list(input.values())[0]
            return converted

    # Pipeline Formatting 
    def pipeline_formatting(self,input):
        input = self.query_formatting(input)

        # Text Inputs
        if self.pipeline_type() == 'text' or self.pipeline_type() == 'input_param':
            return input
        
        # Image Inputs
        elif self.pipeline_type() == 'image':
            if bool(re.match(r'^(http|https)://', input[0])):
                return input
            else:
                self.param_type = {"content_type":"pillow_image"}
                return input
        
        # # Audio Inputs
        # elif self.pipeline_type() == 'audio':
        #     if bool(re.match(r'^(http|https)://', input[0])):
        #         return input
        #     else:
        #         self.param_type = {"content_type":"nplist"}
        #         return input

    def query_conversion(self):
        # Initializing Structure
        inp_skeletal = self.input_skeletal()
        pipeline_type = self.pipeline_type()

        # Single Input Pipeline
        input_format = dict(inp_skeletal[0])
        input_format["data"] = self.pipeline_formatting(self.input)
        input_format["parameters"] = self.param_type
        input_format["datatype"] = self.datatype
        query_list = [input_format]

        # Two Input Pipeline
        if pipeline_type == "input_param":
            param = dict(inp_skeletal[-1])
            param["data"] = self.pipeline_formatting(self.parameters)
            param["parameters"] = self.param_type
            param["datatype"] = self.datatype
            query_list.append(param)

        return query_list
    
    # Final V2 Output
    def v2_input(self):
        query_list = self.query_conversion()
        v2_input = {"inputs":query_list,
                    "outputs":[],
                    "parameters":[]}
    
        return v2_input
