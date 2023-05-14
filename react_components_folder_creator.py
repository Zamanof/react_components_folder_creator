import os

file = open("componentNames.txt", 'r')
folders = file.readlines()
folders = list(map(lambda x: x.strip('\n'), folders))
print(folders)
file.close()
os.mkdir("components")
os.chdir("components")
for folder_name in folders:
    os.mkdir(folder_name)
    os.chdir(folder_name)
    f1 = open(f"{folder_name}.js", "w")
    componentName = folder_name.title().replace('-','')
    print(componentName)
    jsText = f"""import React from "react";

import "./{folder_name}.css";

const {componentName} = () => {"{"}
    return (
        <div>
        <p>Hello</p>
        </div>
    );
{"}"}

export default {componentName};
    """
    f1.write(jsText)
    f2 = open(f"{folder_name}.css", "w")
    f3 = open(f"index.js", "w")
    indTxt = f"""import {componentName}  from './{folder_name}';

export default {componentName};
    """
    f3.write(indTxt)
    f1.close()
    f2.close()
    f3.close()
    os.chdir("..")

