# Use the power of pandas to manage the files on your Android device

```python
pip install list-all-files-recursively
```

```python
from list_all_files_recursively import get_folder_file_complete_path
fi = get_folder_file_complete_path(folders=[r'C:\Users\Gamer\anaconda3\bin',r"C:\yolovtest"])
for file in fi[:10]:
    print(file.folder, file.file, file.path, file.ext)
	
	
	
C:\Users\Gamer\anaconda3\bin libLIEF.dll C:\Users\Gamer\anaconda3\bin\libLIEF.dll .dll
C:\Users\Gamer\anaconda3\bin omptarget.dll C:\Users\Gamer\anaconda3\bin\omptarget.dll .dll
C:\Users\Gamer\anaconda3\bin omptarget.rtl.level0.dll C:\Users\Gamer\anaconda3\bin\omptarget.rtl.level0.dll .dll
C:\Users\Gamer\anaconda3\bin omptarget.rtl.opencl.dll C:\Users\Gamer\anaconda3\bin\omptarget.rtl.opencl.dll .dll
C:\yolovtest devi.txt C:\yolovtest\devi.txt .txt
C:\yolovtest\backgroundimages 2022-10-14 13_13_09-.png C:\yolovtest\backgroundimages\2022-10-14 13_13_09-.png .png
C:\yolovtest\backgroundimages 2022-10-14 13_13_17-Window.png C:\yolovtest\backgroundimages\2022-10-14 13_13_17-Window.png .png
C:\yolovtest\backgroundimages 2022-10-14 13_13_39-.png C:\yolovtest\backgroundimages\2022-10-14 13_13_39-.png .png
C:\yolovtest\backgroundimages 2022-10-14 13_13_46-Window.png C:\yolovtest\backgroundimages\2022-10-14 13_13_46-Window.png .png
C:\yolovtest\backgroundimages 2022-10-14 13_13_54-Window.png C:\yolovtest\backgroundimages\2022-10-14 13_13_54-Window.png .png



from list_all_files_recursively import get_folder_file_complete_path
fi = get_folder_file_complete_path(folders=[r"C:\yolovtest"])
for file in fi[:10]:
    print(file.folder, file.file, file.path, file.ext)
	
	
C:\yolovtest devi.txt C:\yolovtest\devi.txt .txt
C:\yolovtest\backgroundimages 2022-10-14 13_13_09-.png C:\yolovtest\backgroundimages\2022-10-14 13_13_09-.png .png
C:\yolovtest\backgroundimages 2022-10-14 13_13_17-Window.png C:\yolovtest\backgroundimages\2022-10-14 13_13_17-Window.png .png
C:\yolovtest\backgroundimages 2022-10-14 13_13_39-.png C:\yolovtest\backgroundimages\2022-10-14 13_13_39-.png .png
C:\yolovtest\backgroundimages 2022-10-14 13_13_46-Window.png C:\yolovtest\backgroundimages\2022-10-14 13_13_46-Window.png .png
C:\yolovtest\backgroundimages 2022-10-14 13_13_54-Window.png C:\yolovtest\backgroundimages\2022-10-14 13_13_54-Window.png .png
C:\yolovtest\backgroundimages 2022-10-14 13_14_25-Window.png C:\yolovtest\backgroundimages\2022-10-14 13_14_25-Window.png .png
C:\yolovtest\backgroundimages 2022-10-14 21_29_08-Greenshot.png C:\yolovtest\backgroundimages\2022-10-14 21_29_08-Greenshot.png .png
C:\yolovtest\backgroundimages 2022-10-14 21_29_21-Greenshot.png C:\yolovtest\backgroundimages\2022-10-14 21_29_21-Greenshot.png .png
C:\yolovtest\backgroundimages 2022-10-14 21_29_25-Greenshot.png C:\yolovtest\backgroundimages\2022-10-14 21_29_25-Greenshot.png .png

```
