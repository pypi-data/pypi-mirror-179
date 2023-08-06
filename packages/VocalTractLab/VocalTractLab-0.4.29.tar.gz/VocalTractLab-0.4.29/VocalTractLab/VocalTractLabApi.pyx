#####################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#	- This file is a part of the VocalTractLab Python module PyVTL, see https://github.com/paul-krug/VocalTractLab
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#
#	- Copyright (C) 2021, Paul Konstantin Krug, Dresden, Germany
#	- https://github.com/paul-krug/VocalTractLab
#	- Author: Paul Konstantin Krug, TU Dresden
#
#	- License info:
#
#		This program is free software: you can redistribute it and/or modify
#		it under the terms of the GNU General Public License as published by
#		the Free Software Foundation, either version 3 of the License, or
#		(at your option) any later version.
#		
#		This program is distributed in the hope that it will be useful,
#		but WITHOUT ANY WARRANTY; without even the implied warranty of
#		MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#		GNU General Public License for more details.
#		
#		You should have received a copy of the GNU General Public License
#		along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------#
# Load essential packages:

#cimport cVocalTractLabApi # Function defs could be placed here

import numpy as np
cimport numpy as np
import pandas as pd
import ctypes
import os
import warnings
import time
import io

from libcpp cimport bool

import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)

import atexit

from cpython.pycapsule cimport *
#from cpython cimport array
#from libc.stdlib cimport malloc, free


from VocalTractLab.tract_sequence import Sub_Glottal_Sequence, Supra_Glottal_Sequence, Motor_Sequence
from VocalTractLab.targets import Motor_Score
from VocalTractLab.frequency_domain import Transfer_Function
from VocalTractLab.function_tools import save, load
from VocalTractLab.tube_states import Tube_State
import VocalTractLab.audio_tools as AT
import VocalTractLab.function_tools as FT

from tools_mp import multiprocess

import librosa
import multiprocessing as mp
import tqdm
import itertools
from bs4 import BeautifulSoup
#import copy
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################



#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################
#
#	C++ API functions:
#
#####################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------------------------------#
cdef extern from "VocalTractLabApi.h":
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	ctypedef enum SpectrumType:
		NO_RADIATION,
		PISTONINSPHERE_RADIATION,
		PISTONINWALL_RADIATION,
		PARALLEL_RADIATION,
		NUM_RADIATION_OPTIONS,
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	ctypedef enum RadiationType:
		SPECTRUM_UU,
		SPECTRUM_PU,
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	cdef struct TransferFunctionOptions:
		SpectrumType spectrumType,
		RadiationType radiationType,
		bool boundaryLayer,
		bool heatConduction,
		bool softWalls,
		bool hagenResistance,
		bool innerLengthCorrections,
		bool lumpedElements,
		bool paranasalSinuses,
		bool piriformFossa,
		bool staticPressureDrops,
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlCalcTongueRootAutomatically( bool automaticCalculation );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlClose();
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlExportTractSvg( double *tractParams,
		                   const char *fileName
		                   );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlExportTractSvgToStr(
		double *tractParams,
		const char *svgStr,
		);
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlGesturalScoreToAudio( const char *gesFileName,
		                         const char *wavFileName,
		                         double *audio,
		                         int *numSamples,
		                         bool enableConsoleOutput
		                         );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlGesturalScoreToTractSequence( const char *gesFileName, 
		                                 const char *tractSequenceFileName
		                                 );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlGetConstants( int *audioSamplingRate,
		                 int *numTubeSections,
		                 int *numVocalTractParams,
		                 int *numGlottisParams,
		                 int *numAudioSamplesPerTractState,
		                 double *internalSamplingRate
		                 );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlGetDefaultTransferFunctionOptions( TransferFunctionOptions *opts );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlGetGesturalScoreDuration( const char *gesFileName,
		                             int *numAudioSamples,
		                             int *numGestureSamples
		                             );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlGetGlottisParamInfo( char *names,
		                        char *descriptions,
		                        char *units,
		                        double *paramMin,
		                        double *paramMax,
		                        double *paramStandard,
		                        );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlGetTractParamInfo( char *names,
		                      char *descriptions,
		                      char *units,
		                      double *paramMin,
		                      double *paramMax,
		                      double *paramStandard,
		                      );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlGetGlottisParams( const char *shapeName,
	                         double *glottisParams,
	                         );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlGetTractParams( const char *shapeName,
	                       double *tractParams,
	                       );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlGetTransferFunction( double *tractParams,
	                            int numSpectrumSamples,
	                            TransferFunctionOptions *opts,
	                            double *magnitude,
	                            double *phase_rad
	                            );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	void vtlGetVersion( char *version );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlInitialize( const char *speakerFileName );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlInputTractToLimitedTract( double *inTractParams,
		                             double *outTractParams
		                             );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlSegmentSequenceToGesturalScore( const char *segFileName,
		                                   const char *gesFileName,
		                                   bool enableConsoleOutput,
		                                   );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlSynthBlock( double *tractParams,
		               double *glottisParams,
		               int numFrames,
		               int frameStep_samples,
		               double *audio,
		               bool enableConsoleOutput,
		               );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlTractSequenceToAudio( const char *tractSequenceFileName,
		                         const char *wavFileName,
		                         double *audio,
		                         int *numSamples,
		                         );
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlTractToTube(
		double *tractParams,
		double *tubeLength_cm,
		double *tubeArea_cm2,
		int *tubeArticulator,
		double *incisorPos_cm,
		double *tongueTipSideElevation,
		double *velumOpening_cm2
		);
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	int vtlFastTractToTube(
		double *tractParams,
		double *tubeLength_cm,
		double *tubeArea_cm2,
		int *tubeArticulator,
		double *incisorPos_cm,
		double *tongueTipSideElevation,
		double *velumOpening_cm2
		);
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################





#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################
#
#	User functions:
#
#####################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------------------------------#
# 		Single core functions
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def automatic_calculation_of_TRX_and_TRY( bool automatic_calculation = True ):
	cdef bool automaticCalculation = automatic_calculation
	value = vtlCalcTongueRootAutomatically( automaticCalculation )
	#print( value )
	if value != 0:
		raise ValueError('VTL API function vtlCalcTongueRootAutomatically returned the Errorcode: {}  (See API doc for info.)' )
	warnings.warn( 'Automatic calculation of the Tongue Root parameters was set to {}.'.format(automatic_calculation) )
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def get_version():
	cdef char version[32]
	vtlGetVersion( version )
	log.info( 'Compile date of the library: {}'.format( version.decode() ) )
	#if self.params.verbose == True:
	#	log.info( 'Compile date of the library: "%s"' % version.decode() )
	return version.decode()
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def get_constants():
	cdef int audioSamplingRate = -1
	cdef int numTubeSections = -1
	cdef int numVocalTractParams = -1
	cdef int numGlottisParams = -1
	cdef int numAudioSamplesPerTractState = -1
	cdef double internalSamplingRate = -1.0
	value = vtlGetConstants( &audioSamplingRate,
		                     &numTubeSections,
		                     &numVocalTractParams,
		                     &numGlottisParams,
		                     &numAudioSamplesPerTractState,
		                     &internalSamplingRate,
	                         )
	if value != 0:
		raise ValueError('VTL API function vtlGetConstants returned the Errorcode: {}  (See API doc for info.)'.format( value ) )
	constants = {
		'samplerate_audio': int( audioSamplingRate ),
		'samplerate_internal': float( internalSamplingRate ),
		'n_tube_sections': int( numTubeSections ),
		'n_tract_params': int( numVocalTractParams ),
		'n_glottis_params': int( numGlottisParams ),
		'n_samples_per_state': int( numAudioSamplesPerTractState ),
		}
	return constants
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def get_param_info( str params ):
	if params not in [ 'tract', 'glottis' ]:
		log.warning( 'Unknown key in "get_param_info". Key must be "tract" or "glottis". Returning "tract" infos now.' )
		params = 'tract'
	if params == 'tract':
		key = 'n_tract_params'
	elif params == 'glottis':
		key = 'n_glottis_params'
	constants = get_constants()
	names = ( ' ' * 10 * constants[ key ] ).encode()
	descriptions = (' ' * 100 * constants[key]).encode()
	units = (' ' * 10 * constants[key]).encode()
	cdef np.ndarray[ np.float64_t, ndim=1 ] paramMin = np.empty( constants[key], dtype='float64' )
	cdef np.ndarray[ np.float64_t, ndim=1 ] paramMax = np.empty( constants[key], dtype='float64' )
	cdef np.ndarray[ np.float64_t, ndim=1 ] paramStandard = np.empty( constants[key], dtype='float64' )
	if params == 'tract':
		value = vtlGetTractParamInfo( names, descriptions, units, &paramMin[0], &paramMax[0], &paramStandard[0] )
	elif params == 'glottis':
		value = vtlGetGlottisParamInfo( names, descriptions, units, &paramMin[0], &paramMax[0], &paramStandard[0] )
	if value != 0:
		raise ValueError('VTL API function vtlGetTractParamInfo or vtlGetGlottisParamInfo returned the Errorcode: {}  (See API doc for info.)'.format( value ) )
	descriptions = descriptions.decode().replace('\x00', '').strip(' ').strip('').split('\t')
	units = units.decode().replace('\x00', '').strip(' ').strip( '' ).split('\t')
	df = pd.DataFrame( np.array( [ descriptions, units, paramMin, paramMax, paramStandard ] ).T, columns = [ 'description', 'unit', 'min', 'max', 'standard' ] )
	df.index = names.decode().replace('\x00','').strip( ' ' ).strip('').split( '\t' )
	return df
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def get_shape( shape_list, str params = None, return_motor_sequence = True ):
	return get_shapes( shape_list,  params, return_motor_sequence )
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def get_shapes( shape_list, str params = None, return_motor_sequence = True ):
	shape_list = FT.check_if_list_is_valid( shape_list, str )
	constants = get_constants()
	cdef np.ndarray[ np.float64_t, ndim=1 ] tractParams = np.empty( shape = constants[ 'n_tract_params' ],  dtype='float64' )
	cdef np.ndarray[ np.float64_t, ndim=1 ] glottisParams = np.empty( shape = constants[ 'n_glottis_params' ],  dtype='float64' )
	supra_glottal_shapes, sub_glottal_shapes = [], []
	supra_glottal_shape_names, sub_glottal_shape_names = [], []
	for shape in shape_list:
		#print(shape)
		shapeName = shape.encode()
		#if params == 'tract':
		#	value = vtlGetTractParams( shapeName, &tractParams[0, 0] )
		#	supra_glottal_shapes.append( [ tractParams, shape ] )
		#elif params == 'glottis':
		#	value = vtlGetGlottisParams( shapeName, &glottisParams[0, 0] )
		#	sub_glottal_shapes.append( [ glottisParams, shape ] )
		#else:
		value = vtlGetTractParams( shapeName, &tractParams[ 0 ] )
		if value == 0:
			supra_glottal_shapes.append( tractParams.copy() )
			supra_glottal_shape_names.append( shape )
		if value == 2:
			log.info('Specified shape: {} was not found in tract state shapes. Looking for glottal shapes now.'.format( shape ) )
			value = vtlGetGlottisParams( shapeName, &glottisParams[ 0 ] )
			if value == 0:
				sub_glottal_shapes.append( glottisParams.copy() )
				sub_glottal_shape_names.append( shape )
		if value != 0:
			raise ValueError('VTL API function vtlGetTractParams returned the Errorcode: {}  (See API doc for info.)'.format( value ) )
	supra_glottal_sequence_name = ','.join( supra_glottal_shape_names )
	sub_glottal_sequence_name = ','.join( sub_glottal_shape_names )
	#print( 'array shape: {}'.format(np.array( supra_glottal_shapes ).shape )  )
	if len( supra_glottal_shapes ) != 0 and len( sub_glottal_shapes ) != 0:
		supra_glottal_sequence = Supra_Glottal_Sequence( np.array( supra_glottal_shapes ), name = supra_glottal_sequence_name )
		sub_glottal_sequence = Sub_Glottal_Sequence( np.array( sub_glottal_shapes ), name = sub_glottal_sequence_name )
		if return_motor_sequence:
			motor_sequence_name = ','.join( [ supra_glottal_sequence_name, sub_glottal_sequence_name ] )
			return Motor_Sequence( supra_glottal_sequence, sub_glottal_sequence, name = motor_sequence_name )
		else:
			return [ supra_glottal_sequence, sub_glottal_sequence ]
	elif len( supra_glottal_shapes ) != 0:
		return Supra_Glottal_Sequence( np.array( supra_glottal_shapes ), name = supra_glottal_sequence_name )
	elif len( sub_glottal_shapes ) != 0:
		return Sub_Glottal_Sequence( np.array( sub_glottal_shapes ), name = sub_glottal_sequence_name )
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def get_supra_glottal_state( key ):
	return get_param_info( 'tract' )[ key ].to_numpy( dtype = float )
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def get_sub_glottal_state( key ):
	return get_param_info( 'glottis' )[ key ].to_numpy( dtype = float )
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def load_speaker_file( str speaker_file_path ):
	_close()
	_initialize( speaker_file_path )
	log.info( 'Loaded new speakerfile: {}. Overwriting existing settings with the values from the new speaker file.'.format( speaker_file_path ) )
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def load_speaker(
	speaker_name: str,
	):
	speakers = dict(
		jd3 = 'JD3.speaker',
		m18y = 'male_18_years_0_months.speaker',
		m12y = 'male_12_years_0_months.speaker',
		m6y = 'male_6_years_0_months.speaker',
		m3y = 'male_3_years_0_months.speaker',
		f18y = 'female_18_years_0_months.speaker',
		f12y = 'female_12_years_0_months.speaker',
		f6y = 'female_6_years_0_months.speaker',
		f3y = 'female_3_years_0_months.speaker',
		)
	if speaker_name not in speakers.keys():
		raise ValueError(
			'''Unknown speaker name: {}. Available speaker names are: {}.
			If you want to load a custom speaker file, do so via the load_speaker_file() method instead.'''.format(
				speaker_name, speakers.keys(),
				)
			)
	load_speaker_file(
		os.path.join(
			os.path.dirname(__file__),
			'speaker',
			speakers[ speaker_name ],
			) 
		)
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------------------------------#
def get_gestural_score_audio_duration( str ges_file_path, return_samples = True ):
	gesFileName = ges_file_path.encode()
	cdef int numAudioSamples = 0
	numGestureSamples = NULL
	vtlGetGesturalScoreDuration( gesFileName, &numAudioSamples, numGestureSamples )
	n_samples = numAudioSamples
	if return_samples: # returning number of audio samples
		return n_samples
	#else: # returning time in seconds
	#	return n_samples / self.params.samplerate_audio
#---------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------------------------------#
# 		User mp enabled functions
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def change_gestural_score(
	in_ges_file_path_list,
	out_ges_file_path_list,
	modification_kwargs,
	workers: bool = False,
	):
	
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def gestural_score_to_audio(	ges_file_path_list,
								audio_file_path_list = None,
								save_file: bool = True,
								normalize_audio: int = None,
								sr: int = None,
								return_data: bool = False,
								workers: int = None,
								verbose: bool = False,
							):
	ges_file_path_list, audio_file_path_list = FT.check_if_input_lists_are_valid( [ ges_file_path_list, audio_file_path_list ], 
                                                                                  [ str, ( str, type(None) ) ],
	                                                                            )
	args =  [ [ges_file_path, audio_file_path, save_file, normalize_audio, sr, verbose]
		for ges_file_path, audio_file_path in itertools.zip_longest( ges_file_path_list, audio_file_path_list ) ]
	if len( args ) == 1:
		audio_data_list = _gestural_score_to_audio( args[ 0 ] )
	else:
		audio_data_list = _run_multiprocessing( _gestural_score_to_audio, args, return_data, workers )
	return audio_data_list
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def gestural_score_to_tract_sequence(	ges_file_path_list,  
										tract_file_path_list = None, 
										return_data: bool = False,
										workers: int = None,
									):
	ges_file_path_list, tract_file_path_list = FT.check_if_input_lists_are_valid( [ ges_file_path_list, tract_file_path_list ], 
	                                                                              [ str, ( str, type(None) ) ],
	                                                                            )
	args = [ [ges_file_path, tract_file_path, return_data ]
		for ges_file_path, tract_file_path in itertools.zip_longest( ges_file_path_list, tract_file_path_list ) ]
	tract_sequence_list = _run_multiprocessing( _gestural_score_to_tract_sequence, args, return_data, workers )
	return tract_sequence_list
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def segment_sequence_to_gestural_score( seg_file_path_list,
	                                    ges_file_path_list = None,
	                                    workers: int = None,
	                                    verbose: bool = False,
	                                    ):
	seg_file_path_list, ges_file_path_list = FT.check_if_input_lists_are_valid( [ seg_file_path_list, ges_file_path_list ], 
	                                                                            [ str, ( str, type(None) ) ] 
	                                                                          )
	args = [ [ seg_file_path, ges_file_path, verbose ]
		for seg_file_path, ges_file_path in itertools.zip_longest( seg_file_path_list, ges_file_path_list ) ]
	_run_multiprocessing( _segment_sequence_to_gestural_score, args, False, workers )
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def tract_sequence_to_audio( motor_sequence_list,
	                         audio_file_path_list = None,
	                         save_file: bool = True,
	                         normalize_audio: int = -1,
	                         sr: int = None,
	                         return_data: bool = False,
	                         workers: int = None,
	                         verbose: bool = False,
	                         ):
	motor_sequence_list, audio_file_path_list = FT.check_if_input_lists_are_valid( [ motor_sequence_list, audio_file_path_list ], 
																		           [ ( str, Motor_Sequence, Motor_Score ),
	                                                                                 ( str, type(None) ),
	                                                                               ]
	                                                                             )
	args = [ [motor_sequence, audio_file_path, save_file, normalize_audio, sr, verbose]
		for motor_sequence, audio_file_path in itertools.zip_longest( motor_sequence_list, audio_file_path_list ) ]
	if len( args ) <= 4:
		audio_data_list = [ _tract_sequence_to_audio( arg ) for arg in args ]
	else:
		audio_data_list = _run_multiprocessing( _tract_sequence_to_audio, args, return_data, workers )
	return audio_data_list
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def motor_sequence_to_spectrogram(
	motor_sequence_list,
	audio_file_path_list = None,
	spectrogram_file_path_list = None,
	save_file: bool = True,
	normalize_audio: int = -1,
	sr: int = 16000,
	spectrogram_kwargs = AT.standard_16kHz_spectrogram_kwargs,
	return_data: bool = True,
	workers: int = None,
	verbose: bool = False,
	):
	motor_sequence_list, audio_file_path_list, spectrogram_file_path_list = FT.check_if_input_lists_are_valid(
		[ motor_sequence_list, audio_file_path_list, spectrogram_file_path_list ], 
		[ ( str, Motor_Sequence, Motor_Score ), ( str, type(None) ), ( str, type(None) ), ]
	)
	args = [ [
		motor_sequence,
		audio_file_path,
		spectrogram_file_path,
		save_file,
		normalize_audio,
		sr,
		spectrogram_kwargs,
		verbose,
		] for motor_sequence, audio_file_path, spectrogram_file_path in itertools.zip_longest(
			motor_sequence_list,
			audio_file_path_list,
			spectrogram_file_path_list,
		)
	]
	audio_data_list = _run_multiprocessing( _motor_sequence_to_spectrogram, args, return_data, workers )
	return audio_data_list
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def motor_sequence_to_melspectrogram(
	motor_sequence_list,
	audio_file_path_list = None,
	spectrogram_file_path_list = None,
	save_file: bool = True,
	normalize_audio: int = -1,
	sr: int = 16000,
	log_scale = True,
	spectrogram_kwargs = AT.standard_16kHz_spectrogram_kwargs,
	melspectrogram_kwargs = AT.standard_16kHz_melspectrogram_80_kwargs,
	return_data: bool = True,
	workers: int = None,
	verbose: bool = False,
	):
	motor_sequence_list, audio_file_path_list, spectrogram_file_path_list = FT.check_if_input_lists_are_valid(
		[ motor_sequence_list, audio_file_path_list, spectrogram_file_path_list ], 
		[ ( str, Motor_Sequence, Motor_Score ), ( str, type(None) ), ( str, type(None) ), ]
	)
	args = [ [
		motor_sequence,
		audio_file_path,
		spectrogram_file_path,
		save_file,
		normalize_audio,
		sr,
		log_scale,
		spectrogram_kwargs,
		melspectrogram_kwargs,
		verbose,
		] for motor_sequence, audio_file_path, spectrogram_file_path in itertools.zip_longest(
			motor_sequence_list,
			audio_file_path_list,
			spectrogram_file_path_list,
		)
	]
	audio_data_list = _run_multiprocessing( _motor_sequence_to_melspectrogram, args, return_data, workers )
	return audio_data_list
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def tract_sequence_to_limited_tract_sequence( motor_sequence,
	                                          workers: int = None, 
	                                        ):
	if not isinstance( motor_sequence, ( Motor_Sequence, Supra_Glottal_Sequence ) ):
		raise ValueError( 'motor_sequence argument must be Motor_Sequence or Supra_Glottal_Sequence, not {}'.format( type( motor_sequence ) ) )
	tract_param_data = []
	args = [ state for state in motor_sequence.states.to_numpy() ]
	tract_param_data = _run_multiprocessing( _tract_state_to_limited_tract_state, args, True, workers )
	limited_supra_glottal_sequence = Supra_Glottal_Sequence( np.array( tract_param_data ) )
	if isinstance( motor_sequence,  Motor_Sequence ):
		return Motor_Sequence( tract_states = limited_supra_glottal_sequence, glottis_states = motor_sequence.to_sub_glottal_sequence() )
	else:
		return limited_supra_glottal_sequence
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def tract_sequence_to_svg( motor_sequence_list,
	                       svg_dir_list = None,
	                       fps: int = 60,
	                       save_video = False,
	                       workers: int = None,
	                       ):
	motor_sequence_list, svg_dir_list = FT.check_if_input_lists_are_valid( [ motor_sequence_list, svg_dir_list ],
	                                                                       [ ( str, Motor_Sequence ),
	                                                                         ( str, type(None) ),
	                                                                       ]
	                                                                     )
	args = [ [motor_sequence, svg_dir, fps ]
	for motor_sequence, svg_dir in itertools.zip_longest( motor_sequence_list, svg_dir_list ) ]
	_run_multiprocessing( _tract_sequence_to_svg, args, False, workers )
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def supra_glottal_sequence_to_svg(
	supra_glottal_sequence,
	output_directory = None,
	fps: int = 60,
	#save_video = False,
	workers: int = None,
	verbose = True,
	):
	if not isinstance( supra_glottal_sequence, ( Supra_Glottal_Sequence ) ): # could also be motor seq or str
		raise ValueError( 'motor_sequence argument must be Motor_Sequence, not {}'.format( type( supra_glottal_sequence ) ) )
	if fps is None:
		if output_directory is None:
			args = [
				( supra_glottal_state, None )
				for supra_glottal_state in supra_glottal_sequence.states.to_numpy()
				]
		else:
			args = [ 
				( supra_glottal_state, os.path.join( output_directory, '{}.svg'.format( index ) ) )
				for index, supra_glottal_state in enumerate( supra_glottal_sequence.states.to_numpy() )
				]
	else:
		resampled_index = [ round( index * (44100 / 110) / fps ) for index in range( 0, supra_glottal_sequence.length ) ]
		resampled_tract_states = [
			supra_glottal_state for supra_glottal_state in enumerate( supra_glottal_sequence.states.to_numpy() ) if index in resampled_index
			]
		if output_directory is None:
			args = [
				( supra_glottal_state, None )
				for supra_glottal_state in resampled_tract_states
				]
		else:
			args = [ 
				( supra_glottal_state, os.path.join( output_directory, '{}.svg'.format( index ) ) )
				for index, supra_glottal_state in enumerate( resampled_tract_states )
				]
	multiprocess(
		_supra_glottal_state_to_svg,
		args,
		return_data = False,
		verbose = verbose,
		workers = workers,
		)
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def supra_glottal_sequence_to_svg_str(
	supra_glottal_sequence,
	fps: int = 60,
	#save_video = False,
	workers: int = None,
	verbose = True,
	):
	if not isinstance( supra_glottal_sequence, ( Supra_Glottal_Sequence ) ): # could also be motor seq or str
		raise ValueError( 'motor_sequence argument must be Motor_Sequence, not {}'.format( type( supra_glottal_sequence ) ) )
	if fps is None:
		args = [
			( supra_glottal_state )
			for supra_glottal_state in supra_glottal_sequence.states.to_numpy()
			]
	else:
		resampled_index = [ round( index * (44100 / 110) / fps ) for index in range( 0, supra_glottal_sequence.length ) ]
		resampled_tract_states = [
			supra_glottal_state for supra_glottal_state in enumerate( supra_glottal_sequence.states.to_numpy() ) if index in resampled_index
			]
		args = [
			( supra_glottal_state )
			for supra_glottal_state in resampled_tract_states
			]
	data = multiprocess(
		_supra_glottal_state_to_svg_str,
		args,
		return_data = True,
		verbose = verbose,
		workers = workers,
		)
	return data
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def tract_sequence_to_transfer_functions( motor_sequence,
	                                      n_spectrum_samples: int = 8192,
	                                      save_magnitude_spectrum: bool = True,
	                                      save_phase_spectrum: bool = True,
	                                      workers: int = None,
	                                    ):
	if not isinstance( motor_sequence, ( Motor_Sequence, Supra_Glottal_Sequence ) ):
		raise ValueError( 'motor_sequence argument must be Motor_Sequence or Supra_Glottal_Sequence, not {}'.format( type( motor_sequence ) ) )
	if isinstance( motor_sequence, Motor_Sequence ):
		motor_sequence = motor_sequence.to_supra_glottal_sequence()
	tract_param_data = []
	args = [ [ state,
	           n_spectrum_samples,
	           save_magnitude_spectrum,
	           save_phase_spectrum ] 
		for state in motor_sequence.states.to_numpy() ]
	transfer_functions = _run_multiprocessing( _tract_state_to_transfer_function, args, True, workers )
	return transfer_functions
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def tract_sequence_to_tube_states(
	motor_sequence,
	save_tube_length: bool = True,
	save_tube_area: bool = True,
	save_tube_articulator: bool = True,
	save_incisor_position: bool = True,
	save_tongue_tip_side_elevation: bool = True,
	save_velum_opening: bool = True,
	fast_calculation = True,
	workers: int = None,
	):
	if not isinstance( motor_sequence, ( Motor_Sequence, Supra_Glottal_Sequence ) ):
		raise ValueError( 'motor_sequence argument must be Motor_Sequence or Supra_Glottal_Sequence, not {}'.format( type( motor_sequence ) ) )
	if isinstance( motor_sequence, Motor_Sequence ):
		motor_sequence = motor_sequence.to_supra_glottal_sequence()
	tract_param_data = []
	args = [
		[
			state,
			save_tube_length,
			save_tube_area,
			save_tube_articulator,
			save_incisor_position,
			save_tongue_tip_side_elevation,
			save_velum_opening,
			fast_calculation,
			] 
		for state in motor_sequence.states.to_numpy() ]
	if len( args ) <= 4:
		tube_states = [ _tract_state_to_tube_state( arg ) for arg in args ]
	else:
		tube_states = _run_multiprocessing( _tract_state_to_tube_state, args, True, workers )
	return tube_states
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################





#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################
#
#	Internal functions:
#
#####################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------------------------------#
# 		constructor / destructor functions
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _initialize( str speaker_file_path ):
	speakerFileName = speaker_file_path.encode()
	value = vtlInitialize( speakerFileName )
	if value != 0:
		raise ValueError('VTL API function vtlInitialize returned the Errorcode: {}  (See API doc for info.)'.format( value ) )
	#log.info( 'VTL API initialized.' )
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _close():
	value = vtlClose()
	if value != 0:
		raise ValueError('VTL API function vtlClose returned the Errorcode: {}  (See API doc for info.)'.format( value ) )
	#log.info( 'VTL API closed.' )
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------------------------------#
# 		multiprocessing worker functions
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#def _export_tract_svg( args ):
#	tract_state, out_file_path = args
#	cdef np.ndarray[ np.float64_t, ndim=1 ] tractParams = tract_state
#	fileName = out_file_path.encode()
#	constants = get_constants()
#	value = vtlExportTractSvg( &tractParams[0], fileName )
#	if value != 0:
#		raise ValueError('VTL API function vtlExportTractSvg returned the Errorcode: {}  (See API doc for info.)'.format( value ) )
#	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _modify_gestural_score( args ):
	in_ges_file_path, out_ges_file_path = args
	ges_file = open( in_ges_file_path ).read()
	ges_soup = BeautifulSoup( ges_file, 'html.parser' )
	#do manipulations here
	f = open( out_ges_file_path, "w" )
	f.write( ges_soup.prettify( formatter = None ) )
	f.close()
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _gestural_score_change_voice_quality( args ):
	gestural_score_soup, voice_quality_new, voice_quality_old = args
	for element in gestural_score_soup.gestural_score.find( 'gesture_sequence', {'type': 'glottal-shape-gestures'} ):
		try:
			if element.value == voice_quality_old:
				element.value = voice_quality_new
		except Exception: 
			ValueError( 'Error at element: {}, element.value: {}, vq old: {}, vq new: {}'.format( element, element.value, voice_quality_old, voice_quality_new ) )
	return gestural_score_soup
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _gestural_score_change_duration():
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _gestural_score_to_audio( args ):
	# Note that returning the number of samples via numSamples is deprecated, use getGesturalScoreAudioDuration instead!
	time_start = time.time()
	ges_file_path, audio_file_path, save_file, normalize_audio, sr, verbose = args
	constants = get_constants()
	if sr == None:
		sr = constants[ 'samplerate_audio' ]
	if not os.path.exists( ges_file_path ):
		warnings.warn( 'the specified gestural score file path does not exist: {}. API call will be skipped.'.format( ges_file_path ) )
		return
	if save_file:
		audio_file_path = FT.make_output_path( audio_file_path, ges_file_path.rsplit( '.' )[0] + '.wav' )
	if ( save_file and normalize_audio != None ) or ( save_file and sr != constants[ 'samplerate_audio' ] ):
		save_file = False
		return_audio = True
	if save_file == False:
		wavFileName = ''.encode()
	else:
		wavFileName = audio_file_path.encode()
	gesFileName = ges_file_path.encode()
	cdef np.ndarray[ np.float64_t, ndim=1 ] audio
	cdef bool enableConsoleOutput = verbose
	audio = np.zeros( get_gestural_score_audio_duration( ges_file_path, return_samples = True ), dtype='float64' )
	time_synth_start = time.time()
	cdef int numS = 0
	value = vtlGesturalScoreToAudio( gesFileName, wavFileName, &audio[0], &numS, enableConsoleOutput )
	time_synth_end = time.time()
	#print( 'elapsed synthesis time {}'.format( time_synth_end-time_synth_start ) )
	if value != 0:
		raise ValueError('VTL API function vtlGesturalScoreToAudio returned the Errorcode: {}  (See API doc for info.) \
			while processing gestural score file (input): {}, audio file (output): {}'.format(value, ges_file_path, audio_file_path) )
	if sr != constants[ 'samplerate_audio' ]:
		audio = librosa.resample( audio, constants[ 'samplerate_audio' ], sr )
	if normalize_audio != None:
		audio = AT.normalize( audio, normalize_audio )
	if verbose:
		log.info( 'Audio generated from gestural score file: {}'.format( ges_file_path ) )
	if save_file == False and audio_file_path not in ( None, '' ):
		AT.write( audio, audio_file_path, sr )
	time_end = time.time()
	#print( 'elapsed total time {}'.format( time_end-time_start ) )
	return audio
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _gestural_score_to_tract_sequence( args ):
	ges_file_path, tract_file_path, return_sequence = args
	if not os.path.exists( ges_file_path ):
		warnings.warn( 'the specified gestural score file path does not exist: {}. API call will be skipped.'.format( ges_file_path ) )
		return
	gesFileName = ges_file_path.encode()
	tract_file_path = FT.make_output_path( tract_file_path, ges_file_path.rsplit('.')[0] + '.tract' )
	tractSequenceFileName = tract_file_path.encode()
	value = vtlGesturalScoreToTractSequence( gesFileName, tractSequenceFileName )
	if value != 0:
		raise ValueError('VTL API function vtlGesturalScoreToTractSequence returned the Errorcode: {}  (See API doc for info.) \
			while processing gestural score file (input): {}, tract sequence file (output): {}'.format(value, ges_file_path, tract_file_path) )
	log.info( 'Created tractsequence file {} from gestural score file: {}'.format( tract_file_path, ges_file_path ) )
	if return_sequence:
		return Motor_Sequence.from_tract_file( tract_file_path )
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _segment_sequence_to_gestural_score( args ):
	seg_file_path, ges_file_path, verbose = args
	if not os.path.exists( seg_file_path ):
		warnings.warn( 'the specified segment sequence file path does not exist: {}. API call will be skipped.'.format( seg_file_path ) )
		return
	ges_file_path = FT.make_output_path( ges_file_path, seg_file_path.rsplit('.')[0] + '.ges' )
	segFileName = seg_file_path.encode()
	gesFileName = ges_file_path.encode()
	cdef bool enableConsoleOutput = verbose
	value = vtlSegmentSequenceToGesturalScore( segFileName, gesFileName, enableConsoleOutput )
	if value != 0:
		raise ValueError('VTL API function vtlSegmentSequenceToGesturalScore returned the Errorcode: {}  (See API doc for info.) \
			while processing segment sequence file (input): {}, gestural score file (output): {}'.format(value, seg_file_path, ges_file_path) )
	log.info( 'Created gestural score from segment sequence file: {}'.format( seg_file_path ) )
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _synth_block( args ):
	motor_sequence, state_samples, verbose = args
	if state_samples == None:
		constants = get_constants()
		state_samples = constants[ 'n_samples_per_state' ]
	cdef int numFrames = motor_sequence.length
	cdef np.ndarray[ np.float64_t, ndim=1 ] tractParams = motor_sequence.to_supra_glottal_states().ravel()
	cdef np.ndarray[ np.float64_t, ndim=1 ] glottisParams = motor_sequence.to_sub_glottal_states().ravel()
	cdef int frameStep_samples = state_samples
	cdef np.ndarray[ np.float64_t, ndim=1 ] audio = np.zeros( motor_sequence.length * state_samples, dtype='float64' )
	cdef bool enableConsoleOutput = verbose
	value = vtlSynthBlock( &tractParams[0], &glottisParams[0], numFrames, frameStep_samples, &audio[0], enableConsoleOutput )
	if value != 0:
		raise ValueError( 'VTL API function vtlSynthBlock returned the Errorcode: {}  (See API doc for info.)'.format( value ) )
	return audio
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _tract_sequence_to_audio( args ):
	# Note that returning the number of samples via numSamples is deprecated, use getGesturalScoreAudioDuration instead!
	motor_sequence_data, audio_file_path, save_file, normalize_audio, sr, verbose = args
	if isinstance( motor_sequence_data, str ):
		tract_file_path = motor_sequence_data
		if not os.path.exists( tract_file_path ):
			warnings.warn( 'the specified tract sequence file path does not exist: {}. API call will be skipped.'.format( tract_file_path ) )
			return
		motor_sequence = Motor_Sequence.from_tract_file( tract_file_path )
	elif isinstance( motor_sequence_data, Motor_Score ):
		motor_score = motor_sequence_data
		motor_sequence = motor_score.to_motor_sequence()
	else:
		motor_sequence = motor_sequence_data
	audio = _synth_block( ( motor_sequence, None, verbose ) )
	constants = get_constants()
	if sr == None:
		sr = constants[ 'samplerate_audio' ]
	if save_file:
		audio_file_path = FT.make_output_path( audio_file_path, motor_sequence.name.rsplit( '.' )[0] + '.wav' )
	if sr != constants[ 'samplerate_audio' ]:
		audio = librosa.resample(
			y = audio,
			orig_sr = constants[ 'samplerate_audio' ],
			target_sr = sr,
			)
	if normalize_audio != None:
		audio = AT.normalize( audio, normalize_audio )
	if save_file:
		AT.write( audio, audio_file_path, sr )
	log.info( 'Audio generated from motor_sequence: {}'.format( motor_sequence.name ) )
	return audio
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _motor_sequence_to_spectrogram( args ):
	( 
		motor_sequence_data,
		audio_file_path,
		spectrogram_file_path,
		save_file,
		normalize_audio,
		sr,
		spectrogram_kwargs,
		verbose,
	) = args
	audio_args = ( motor_sequence_data, audio_file_path, save_file, normalize_audio, sr, verbose )
	audio = _tract_sequence_to_audio( audio_args )
	spectrogram = np.abs( librosa.stft( y = audio, **spectrogram_kwargs ) )**2
	if spectrogram_file_path != None: # TODO: replace with saveFile
		spectrogram_file_path = FT.make_output_path( spectrogram_file_path, '_spectrogram.pkl.gzip' )#motor_sequence.name.rsplit( '.' )[0] +
		save( spectrogram, spectrogram_file_path )
	return spectrogram
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _motor_sequence_to_melspectrogram( args ):
	( 
		motor_sequence_data,
		audio_file_path,
		melspectrogram_file_path,
		save_file,
		normalize_audio,
		sr,
		log_scale,
		spectrogram_kwargs,
		melspectrogram_kwargs,
		verbose,
	) = args
	audio_args = ( motor_sequence_data, audio_file_path, save_file, normalize_audio, sr, verbose )
	audio = _tract_sequence_to_audio( audio_args )
	#spectrogram_kwargs = dict()
	spectrogram = np.abs( librosa.stft( y = audio, **spectrogram_kwargs ) )**2
	melspectrogram = librosa.feature.melspectrogram( S = spectrogram, **melspectrogram_kwargs )
	if log_scale == True:
		melspectrogram = librosa.power_to_db( melspectrogram )
	if melspectrogram_file_path != None: # TODO: replace with saveFile
		melspectrogram_file_path = FT.make_output_path( melspectrogram_file_path, '_spectrogram.pkl.gzip' )#motor_sequence.name.rsplit( '.' )[0] +
		save( melspectrogram, melspectrogram_file_path )
	return melspectrogram
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#def _motor_sequence_to_melspectrogram( args ):
#	( 
#		motor_sequence_data,
#		audio_file_path,
#		save_file,
#		normalize_audio,
#		sr,
#		spectrogram_file_path,
#		melspectrogram_file_path,
#		spectrogram_kwargs,
#		melspectrogram_kwargs,
#		verbose,
#	) = args
#	audio_args = ( motor_sequence_data, audio_file_path, save_file, normalize_audio, sr, verbose )
#	audio = self._tract_sequence_to_audio( audio_args )
#	spectrogram = np.abs( librosa.stft( y = audio, **spectrogram_kwargs ) )**2
#	melspectrogram = librosa.feature.melspectrogram( S = spectrogram, sr = sr, **melspectrogram_kwargs )
#	if spectrogram_file_path != None:
#		save( spectrogram, spectrogram_file_path )
#	if melspectrogram_file_path != None:
#		save( melspectrogram, melspectrogram_file_path )
#	return melspectrogram
##---------------------------------------------------------------------------------------------------------------------------------------------------#
#def _motor_sequence_to_mfcc( args ):
#	( 
#		motor_sequence_data,
#		audio_file_path,
#		save_file,
#		normalize_audio,
#		sr,
#		spectrogram_file_path,
#		melspectrogram_file_path,
#		mfcc_file_path,
#		spectrogram_kwargs,
#		melspectrogram_kwargs,
#		mfcc_kwargs,
#		verbose,
#	) = args
#	audio_args = ( motor_sequence_data, audio_file_path, save_file, normalize_audio, sr, verbose )
#	audio = self._tract_sequence_to_audio( audio_args )
#	spectrogram = np.abs( librosa.stft( y = audio, **spectrogram_kwargs ) )**2
#	melspectrogram = librosa.feature.melspectrogram( S = spectrogram, sr = sr, **melspectrogram_kwargs )
#	mfcc = librosa.feature.mfcc( S = librosa.power_to_b( dmelspectrogram ), sr = sr, **mfcc_kwargs )
#	if spectrogram_file_path != None:
#		save( spectrogram, spectrogram_file_path )
#	if melspectrogram_file_path != None:
#		save( melspectrogram, melspectrogram_file_path )
#	if mfcc_file_path != None:
#		save( mfcc, mfcc_file_path )
#	return mfcc
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _tract_state_to_limited_tract_state( args ):
	tract_state = args
	constants = get_constants()
	cdef np.ndarray[ np.float64_t, ndim=1 ] inTractParams = tract_state.ravel()
	cdef np.ndarray[ np.float64_t, ndim=1 ] outTractParams = np.zeros( constants[ 'n_tract_params' ], dtype='float64' )
	vtlInputTractToLimitedTract( &inTractParams[0], &outTractParams[0] )
	return outTractParams
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _tract_sequence_to_svg( args ):
	motor_sequence, svg_dir, fps = args
	if isinstance( motor_sequence, str ) :
		tract_file_path = motor_sequence
		if not os.path.exists( tract_file_path ) :
			warnings.warn( 'the specified tract sequence file path does not exist: {}. API call will be skipped.'.format( tract_file_path ) )
			return
		motor_sequence = Motor_Sequence.from_tract_file( tract_file_path )
	#elif isinstance( motor_sequence, ts.Target_Sequence ) :
	#	target_sequence = motor_sequence
	#	motor_sequence = target_sequence.to_motor_sequence()
	#else:
	#	#pass
	#	#motor_sequence = motor_sequence_data
	svg_dir = FT.make_output_dir( svg_dir, motor_sequence.name.rsplit('.')[0] + '_svg' )
	constants = get_constants()
	cdef np.ndarray[np.float64_t, ndim = 1] tractParams = np.zeros( constants['n_tract_params'], dtype = 'float64' )
	resampled_index = [ round(index * (44100 / 110) / fps) for index in range( 0, motor_sequence.length ) ]
	resampled_tract_states = [ [ index, tract_state ] for index, tract_state in enumerate( motor_sequence.states.to_numpy() ) if index in resampled_index ]
	for pair in resampled_tract_states:
		index, tract_state = pair
		tractParams = tract_state.ravel()
		fileName = ( svg_dir + '/tract_{}.svg'.format( index ) ).encode()
		vtlExportTractSvg( &tractParams[0], fileName )
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _supra_glottal_state_to_svg( args ):
	supra_glottal_state, svg_path = args
	if svg_path is None:
		fileName = io.BytesIO( b'abcd' ).read()
	else:
		fileName = svg_path.encode()
	constants = get_constants()
	cdef np.ndarray[np.float64_t, ndim = 1] tractParams = np.zeros(
		constants['n_tract_params'],
		dtype = 'float64',
		)
	tractParams = supra_glottal_state.ravel()
	vtlExportTractSvg(
		&tractParams[0],
		fileName,
		)
	return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _supra_glottal_state_to_svg_str( args ):
	supra_glottal_state = args
	svgStr = ( ' ' * 10000 ).encode()
	constants = get_constants()
	cdef np.ndarray[np.float64_t, ndim = 1] tractParams = np.zeros(
		constants['n_tract_params'],
		dtype = 'float64',
		)
	tractParams = supra_glottal_state.ravel()
	vtlExportTractSvgToStr(
		&tractParams[0],
		svgStr,
		)
	return svgStr.decode()
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _tract_state_to_transfer_function( args ):
	tract_state, n_spectrum_samples, save_magnitude_spectrum, save_phase_spectrum = args
	magnitude_spectrum = None
	phase_spectrum = None
	cdef int numSpectrumSamples = n_spectrum_samples
	cdef np.ndarray[ np.float64_t, ndim=1 ] tractParams = tract_state.ravel()
	cdef np.ndarray[ np.float64_t, ndim=1 ] magnitude = np.zeros( n_spectrum_samples, dtype='float64' )
	cdef np.ndarray[ np.float64_t, ndim=1 ] phase_rad = np.zeros( n_spectrum_samples, dtype='float64' )
	value = vtlGetTransferFunction( &tractParams[0],
	                                numSpectrumSamples,
	                                NULL,
	                                &magnitude[0],
	                                &phase_rad[0],
	                              )
	if save_magnitude_spectrum:
		magnitude_spectrum = np.array( magnitude )
	if save_phase_spectrum:
		phase_spectrum = np.array( phase_rad )
	return Transfer_Function( magnitude_spectrum, phase_spectrum, n_spectrum_samples )
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _tract_state_to_tube_state( args ):
	[
		tract_state,
		save_tube_length,
		save_tube_area,
		save_tube_articulator,
		save_incisor_position,
		save_tongue_tip_side_elevation,
		save_velum_opening,
		fast_calculation,
		] = args
	tube_length = None
	tube_area = None
	tube_articulator = None
	incisor_position = None
	tongue_tip_side_elevation = None
	velum_opening = None
	constants = get_constants()
	cdef np.ndarray[ np.float64_t, ndim=1 ] tractParams = tract_state.ravel()
	cdef np.ndarray[ np.float64_t, ndim=1 ] tubeLength_cm = np.zeros( constants[ 'n_tube_sections' ], dtype='float64' )
	cdef np.ndarray[ np.float64_t, ndim=1 ] tubeArea_cm2 = np.zeros( constants[ 'n_tube_sections' ], dtype='float64' )
	cdef np.ndarray[ int, ndim=1 ] tubeArticulator = np.zeros( constants[ 'n_tube_sections' ], dtype='i' )
	cdef double incisorPos_cm = 0.0
	cdef double tongueTipSideElevation = 0.0
	cdef double velumOpening_cm2 = 0.0
	if fast_calculation:
		vtlFastTractToTube(
			&tractParams[0],
			&tubeLength_cm[0],
			&tubeArea_cm2[0],
			&tubeArticulator[0],
			&incisorPos_cm,
			&tongueTipSideElevation,
			&velumOpening_cm2
			)
	else:
		vtlTractToTube(
			&tractParams[0],
			&tubeLength_cm[0],
			&tubeArea_cm2[0],
			&tubeArticulator[0],
			&incisorPos_cm,
			&tongueTipSideElevation,
			&velumOpening_cm2
			)
	if save_tube_length:
		tube_length = np.array( tubeLength_cm )
	if save_tube_area:
		tube_area = np.array( tubeArea_cm2 )
	if save_tube_articulator:
		tube_articulator = np.array( tubeArticulator )
	if save_incisor_position:
		incisor_position = incisorPos_cm
	if save_tongue_tip_side_elevation:
		tongue_tip_side_elevation = tongueTipSideElevation
	if save_velum_opening:
		velum_opening = velumOpening_cm2
	return Tube_State( tube_length, tube_area, tube_articulator, incisor_position, tongue_tip_side_elevation, velum_opening )
#---------------------------------------------------------------------------------------------------------------------------------------------------#






#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _run_multiprocessing( function, args, return_data, workers ):
	if workers == None:
		workers = mp.cpu_count()
	pool = mp.Pool( workers )
	tasks = ( ( function, x ) for x in args)
	data = None
	if return_data:
		data = []
		for x in tqdm.tqdm( pool.imap( _worker, tasks ), total=len( args ) ):
			data.append( x )
	else:
		for x in tqdm.tqdm( pool.imap( _worker, tasks ), total=len( args ) ):
			pass
	pool.close()
	pool.join()
	return data
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def _worker( args ):
	function, arg = args
	return function( arg )
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################





#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################
#
#	Code to execute at module import:
#
#####################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------------------------------#
atexit.register( _close )
_initialize( os.path.join( os.path.dirname(__file__), 'speaker/JD3.speaker' ) )
#---------------------------------------------------------------------------------------------------------------------------------------------------#


#####################################################################################################################################################