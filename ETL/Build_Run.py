import ETL
import Commands

#License:ThisIsMyStuffBitch



def get_extraction_params(path):
	return ExtractionCommand()

def get_transform_params(path):
	return TransformCommand()

def get_load_params(path):
	return LoadingCommand()



def build_pipeline():

	#we get the schemes from the pipeline specs file
	print('Getting achitecture Specs...')
	extract_params = get_extraction_params('placeholder')
	transform_params = get_transform_params('placeholder')
	load_params = get_load_params('placeholder')

	print('Building...\n')
	#we can now build the ETL components
	extract_comp = Extractor(extract_params)
	transform_comp = Transforms(transform_params)
	load_comp = Loader(load_params)

	print('done.')
	return Pipeline(extract_comp, transform_comp, load_comp)



def run(pipeline_model):

 	while True:
 		pipeline_model.get_batch()

 		



if __name__ == '__main__':
	etl = build_pipeline()
	run(etl)


