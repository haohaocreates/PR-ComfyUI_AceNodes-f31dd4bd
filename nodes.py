import torch
import numpy as np
from PIL import Image

class AnyType(str):
    def __eq__(self, _) -> bool:
        return True

    def __ne__(self, __value: object) -> bool:
        return False

any = AnyType("*")


class ACE_Integer:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "int": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "execute"
    CATEGORY = "Ace Nodes"

    def execute(self, int):
        return (int,)
    
class ACE_Float:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float": ("FLOAT", {"default": 0.0}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "execute"
    CATEGORY = "Ace Nodes"

    def execute(self, float):
        return (float,)

class ACE_Text:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": '', "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "Ace Nodes"

    def execute(self, text):
        return (text,)
    
class ACE_Seed:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "execute"
    CATEGORY = "Ace Nodes"

    def execute(self, seed):
        return (seed,)
    
class ACE_TextConcatenate:
    @ classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text1": ("STRING", {"multiline": True, "forceInput": True}),                
                "text2": ("STRING", {"multiline": True, "forceInput": True}), 
                "separator": ("STRING", {"default": ", ", "multiline": False}),                
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "Ace Nodes"

    def execute(self, text1, text2, separator):
        return (text1 + separator + text2,)
    
class ACE_TextInputSwitch2Way:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": ("INT", {"default": 1, "min": 1, "max": 2}),
            },
            "optional": {
                "text1": ("STRING", {"default": '', "multiline": True, "forceInput": True}),
                "text2": ("STRING", {"default": '', "multiline": True, "forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "Ace Nodes"

    def execute(self, input, text1='', text2=''):
        if input <= 1:
            return (text1,)
        else:
            return (text2,)  

class ACE_TextInputSwitch4Way:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": ("INT", {"default": 1, "min": 1, "max": 4}),
            },
            "optional": {
                "text1": ("STRING", {"default": '', "multiline": True, "forceInput": True}),
                "text2": ("STRING", {"default": '', "multiline": True, "forceInput": True}),
                "text3": ("STRING", {"default": '', "multiline": True, "forceInput": True}),
                "text4": ("STRING", {"default": '', "multiline": True, "forceInput": True}),  
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "Ace Nodes"

    def execute(self, input, text1='', text2='', text3='', text4=''):
        if input <= 1:
            return (text1,)
        elif input == 2:
            return (text2,)
        elif input == 3:
            return (text3,)
        else:
            return (text4,)    

class ACE_TextInputSwitch8Way:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": ("INT", {"default": 1, "min": 1, "max": 8}),
            },
            "optional": {
                "text1": ("STRING", {"default": '', "multiline": True, "forceInput": True}),
                "text2": ("STRING", {"default": '', "multiline": True, "forceInput": True}),
                "text3": ("STRING", {"default": '', "multiline": True, "forceInput": True}),
                "text4": ("STRING", {"default": '', "multiline": True, "forceInput": True}),  
                "text5": ("STRING", {"default": '', "multiline": True, "forceInput": True}),
                "text6": ("STRING", {"default": '', "multiline": True, "forceInput": True}),
                "text7": ("STRING", {"default": '', "multiline": True, "forceInput": True}),
                "text8": ("STRING", {"default": '', "multiline": True, "forceInput": True}),  
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "Ace Nodes"

    def execute(self, input, text1='', text2='', text3='', text4='', text5='', text6='', text7='', text8=''):
        if input <= 1:
            return (text1,)
        elif input == 2:
            return (text2,)
        elif input == 3:
            return (text3,)
        elif input == 4:
            return (text4,)
        elif input == 5:
            return (text5,)
        elif input == 6:
            return (text6,)
        elif input == 7:
            return (text7,)
        else:
            return (text8,)  
        
class ACE_TextList:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":{
                "list_text": ("STRING", {"default": '', "multiline": True}),              
            }
        }

    RETURN_TYPES = ("STRING",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "execute"
    CATEGORY = "Ace Nodes"
    
    def execute(self, list_text):
        lines = list_text.split('\n')
        list_out = [x.strip() for x in lines if x.strip()]
        return (list_out,)
    
class ACE_TextPreview:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            }
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "execute"
    CATEGORY = "Ace Nodes"

    def execute(self, text):
        return {"ui": {"text": text}, "result": (text,)}
    
class ACE_TextSelector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":{
                "list_text": ("STRING", {"default": '', "multiline": True}),    
                "select": ("INT", {"default": 0, "min": 0}),      
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "Ace Nodes"
    
    def execute(self, list_text, select):
        lines = list_text.split('\n')
        list_out = [x.strip() for x in lines if x.strip()]
        select = max(min(select, len(list_out)-1), 0)
        return (list_out[select],)
    
class ACE_TextToResolution:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":{
                "text": ("STRING", {"default": '', "forceInput": True}),
            }
        }

    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("WIDTH", "HEIGHT",)
    FUNCTION = "execute"
    CATEGORY = "Ace Nodes"
    
    def execute(self, text):
        width, height = text.strip().split(" ")[0].split("x")
        width, height = int(width), int(height)
        return (width,height,)

class ACE_ImageConstrain:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "max_width": ("INT", {"default": 1024, "min": 0}),
                "max_height": ("INT", {"default": 1024, "min": 0}),
                "min_width": ("INT", {"default": 0, "min": 0}),
                "min_height": ("INT", {"default": 0, "min": 0}),
                "crop_if_required": ("BOOLEAN", {"default": False, "label_on": "yes", "label_off": "no"}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "execute"
    CATEGORY = "Ace Nodes"

    def execute(self, images, max_width, max_height, min_width, min_height, crop_if_required):
        results = []
        for image in images:
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8)).convert("RGB")

            current_width, current_height = img.size
            aspect_ratio = current_width / current_height

            constrained_width = max(min(current_width, min_width), max_width)
            constrained_height = max(min(current_height, min_height), max_height)

            if constrained_width / constrained_height > aspect_ratio:
                constrained_width = max(int(constrained_height * aspect_ratio), min_width)
                if crop_if_required:
                    constrained_height = int(current_height / (current_width / constrained_width))
            else:
                constrained_height = max(int(constrained_width / aspect_ratio), min_height)
                if crop_if_required:
                    constrained_width = int(current_width / (current_height / constrained_height))

            resized_image = img.resize((constrained_width, constrained_height), Image.LANCZOS)

            if crop_if_required and (constrained_width > max_width or constrained_height > max_height):
                left = max((constrained_width - max_width) // 2, 0)
                top = max((constrained_height - max_height) // 2, 0)
                right = min(constrained_width, max_width) + left
                bottom = min(constrained_height, max_height) + top
                resized_image = resized_image.crop((left, top, right, bottom))

            resized_image = np.array(resized_image).astype(np.float32) / 255.0
            resized_image = torch.from_numpy(resized_image)[None,]
            results.append(resized_image)
                
        return (results,)
    

NODE_CLASS_MAPPINGS = {
    "ACE_Integer"               : ACE_Integer,
    "ACE_Float"                 : ACE_Float,
    "ACE_Text"                  : ACE_Text,
    "ACE_Seed"                  : ACE_Seed,
    "ACE_TextConcatenate"       : ACE_TextConcatenate,
    "ACE_TextInputSwitch2Way"   : ACE_TextInputSwitch2Way,
    "ACE_TextInputSwitch4Way"   : ACE_TextInputSwitch4Way,
    "ACE_TextInputSwitch8Way"   : ACE_TextInputSwitch8Way,
    "ACE_TextList"              : ACE_TextList,
    "ACE_TextPreview"           : ACE_TextPreview,
    "ACE_TextSelector"          : ACE_TextSelector,
    "ACE_TextToResolution"      : ACE_TextToResolution,
    "ACE_ImageConstrain"        : ACE_ImageConstrain,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ACE_Integer"               : "🅐 Integer",
    "ACE_Float"                 : "🅐 Float",
    "ACE_Text"                  : "🅐 Text",
    "ACE_Seed"                  : "🅐 Seed",
    "ACE_TextConcatenate"       : "🅐 Text Concatenate",
    "ACE_TextInputSwitch2Way"   : "🅐 Text Input Switch (2 way)",
    "ACE_TextInputSwitch4Way"   : "🅐 Text Input Switch (4 way)",
    "ACE_TextInputSwitch8Way"   : "🅐 Text Input Switch (8 way)",
    "ACE_TextList"              : "🅐 Text List",
    "ACE_TextPreview"           : "🅐 Text Preview",
    "ACE_TextSelector"          : "🅐 Text Selector",
    "ACE_TextToResolution"      : "🅐 Text To Resolution",
    "ACE_ImageConstrain"        : "🅐 Image Constrain",
}