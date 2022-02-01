from   os        import path,system


def exportLib():
	system("export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/lucas/.mujoco/mujoco210/bin")
	system("export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia")

def xacro(model_path, model_name):

	if path.exists(model_path): 
		system(f"xacro  {model_path}{model_name}.xacro > {model_path}{model_name}.xml")
		# print(f"xacro  {model_path}{model_name}.xacro > {model_path}{model_name}.xml")
	else:
		print('Não encontrei o arquivo')