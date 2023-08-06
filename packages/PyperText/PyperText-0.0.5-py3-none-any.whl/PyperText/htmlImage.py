from .htmlWidget import htmlWidget
from .tools import exists,isUrl,getHeight,getWidth
class Image(htmlWidget):
    '''
    HTML Image Class derived from htmlWidget
    '''
    code=""
    type="Image"
    def __init__(self,path:str)->None:
        if exists(path):self.file=path
        else:
            print("Image: Image path is incorrect, the file does not exist.")
            return None
        self.text=""
        self.options:list[str]=list[str]()
        self.style:list[str]=list[str]()
        self.header="<img >"
        self.CustomHeader=False
        self.image=""
    def setAlternativeText(self,text:str)->None:
        '''
        Set text for if image fails to load.
        '''
        self.text=text
        self.CustomHeader=True
    def setImage(self,image:str)->None:
        '''
        Set the image of the widget
        '''
        if(exists(image) or isUrl(image)):self.image=image
        self.CustomHeader=True
    def _buildImage(self)->None:
        '''
        Builds image to options
        '''
        self.options.insert(0,f"src=\"{self.file}\"")
    def _buildOptions(self)->str:
        '''
        build options to string to be finalized
        '''
        final=""
        if "style" in self.options:
            for i in self.options:
                if i.__includes__("style"):self.style=i.split("style=")[1].split(";")[0]  # type: ignore
                else:continue
            del self.options[self.options.index("style")]
        for i in self.options:final+=i+" "
        return final
    def _buildStyle(self)->str:
        final=""
        for i in final:
            if i.endswith(";"):final+=i
            else:final+=i+";"
        return final
    def _buildText(self)->None:
        '''
        build text to alt
        '''
        self.options.append(f"alt=\"{self.text}\"")
    def finalize(self)->None:
        '''
        Finalize the Image to self.code
        '''
        if self.CustomHeader:
            print("Image: Creating Image with Custom Header")
            self._buildImage()
            self._buildText()
            if self._buildStyle() =="" or self._buildStyle==" ":self.code=self.header.rstrip(self.header[-1])+f" {self._buildOptions()}>"
            else:self.code=self.header.rstrip(self.header[-1])+ f"style=\"{self._buildStyle()}\" {self._buildOptions()}>"
        else:
            print("Image: Creating Image with Default Header")
            self.code=self.header.rstrip(self.header[-1])+f" alt=\"{self.text}\"src=\"{self.image}\" width=\"{getWidth(self.image)}\" height=\"{getHeight(self.image)}\">"


if __name__=="__main__":pass