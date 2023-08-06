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
import VocalTractLab.VocalTractLabApi as vtl
import VocalTractLab.plotting_tools as PT
from VocalTractLab.plotting_tools import finalize_plot
from VocalTractLab.plotting_tools import get_plot
from VocalTractLab.plotting_tools import get_plot_limits
import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#####################################################################################################################################################




#---------------------------------------------------------------------------------------------------------------------------------------------------#
def multiple_formatter( denominator=2, number=np.pi, latex='\\pi' ):
	def gcd(a, b):
		while b:
			a, b = b, a%b
		return a
	def _multiple_formatter(x, pos):
		den = denominator
		num = np.int(np.rint(den*x/number))
		com = gcd(num,den)
		(num,den) = (int(num/com),int(den/com))
		if den==1:
			if num==0:
				return r'$0$'
			if num==1:
				 return r'$%s$'%latex
			elif num==-1:
				return r'$-%s$'%latex
			else:
				return r'$%s%s$'%(num,latex)
		else:
			if num==1:
				return r'$\frac{%s}{%s}$'%(latex,den)
			elif num==-1:
				return r'$\frac{-%s}{%s}$'%(latex,den)
			else:
				return r'$\frac{%s%s}{%s}$'%(num,latex,den)
	return _multiple_formatter
#---------------------------------------------------------------------------------------------------------------------------------------------------#
class Multiple:
	def __init__(self, denominator=2, number=np.pi, latex='\\pi'):
		self.denominator = denominator
		self.number = number
		self.latex = latex
	def locator(self):
		return plt.MultipleLocator(self.number / self.denominator)
	def formatter(self):
		return plt.FuncFormatter(multiple_formatter(self.denominator, self.number, self.latex))
#---------------------------------------------------------------------------------------------------------------------------------------------------#



#####################################################################################################################################################
class Transfer_Function():
	def __init__( self, 
		          magnitude_spectrum: np.ndarray,
		          phase_spectrum: np.ndarray,
		          n_spectrum_samples: int,
		          name: str = 'transfer_function'
		          ):
		if not isinstance( n_spectrum_samples, int ):
			raise ValueError( 'n_spectrum_samples must be an integer and should be a power of 2! Passed type is: {}'.format( type( n_spectrum_samples ) ) )
		self.constants = vtl.get_constants()
		self.delta_frequency = self.constants[ 'samplerate_audio' ] / n_spectrum_samples
		max_bin = round( n_spectrum_samples / self.delta_frequency )
		self.n_spectrum_samples = n_spectrum_samples
		if isinstance( magnitude_spectrum, np.ndarray ):
			self.magnitude_spectrum = magnitude_spectrum[ : max_bin ]
		else:
			self.magnitude_spectrum = None
		if isinstance( phase_spectrum, np.ndarray ):
			self.phase_spectrum = phase_spectrum[ : max_bin ]
		else:
			self.phase_spectrum = None
		self.data = dict( frequency = self.magnitude_spectrum, phase = self.phase_spectrum )
		self.formants = self.get_formants()
		self.f1, self.f2, self.f3, self.f4 = self.formants
		return
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	def get_formants( self, peak_distance = 1, sr = 44100 ):
		sr = self.constants[ 'samplerate_audio' ]
		peaks, _ = find_peaks( self.magnitude_spectrum, distance = peak_distance )
		peaks = [ peak * sr/self.n_spectrum_samples for peak in peaks ]
		while peaks[ 0 ] < 100:
			del peaks[ 0 ]
		if len( peaks ) < 4:
			peaks.extend( [ None for _ in range( 0, 4 - len( peaks ) ) ] )
		elif len( peaks ) > 4:
			peaks = peaks[ : 4 ]
		return peaks
#---------------------------------------------------------------------------------------------------------------------------------------------------#
	def plot( self,
		      parameters = [ 'frequency', 'phase' ],
		      plot_formants = True,
		      axs: list = None,
		      plot_kwargs: list = [ dict( color = 'navy' ), dict( color = 'darkorange' ) ],
		      **kwargs,
		      ): #, scale = 'dB' ):
		figure, axs = get_plot( n_rows = len( parameters ), axs = axs )
		for index, parameter in enumerate( parameters ):
			if parameter == 'frequency':
				y = librosa.amplitude_to_db( self.data[ parameter ] )
				continuities = [ slice( 0, len(y) ) ]
				y_title = 'Intensity [dB]'
				#_min = np.min( y )
				#_max = np.max( y )
				#axs[ index ].set( ylim = [ _min - 0.1 * np.abs( _max - _min ), _max + 0.1 * np.abs( _max - _min ) ] )
				axs[ index ].set( ylim = get_plot_limits( y ) )
				axs[ index ].locator_params( axis = 'y', nbins = 4 )
			elif parameter == 'phase':
				continuities = []
				y = self.data[ parameter ]
				tmp_idx = 0
				for idx in range( 0, len(y) - 1 ):
					if np.abs( y[idx] - y[idx+1] ) > 1.5:
						continuities.append( slice( tmp_idx, idx+1 ) )
						tmp_idx = idx + 1
				if tmp_idx != len( y ):
					continuities.append( slice( tmp_idx, len( y ) ) )

				y = self.data[ parameter ]
				y_title = 'Phase'
				axs[ index ].yaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
				#axs[ index ].yaxis.set_minor_locator(plt.MultipleLocator(np.pi / 12))
				axs[ index ].yaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))
				axs[ index ].set( ylim = [ -3.76, 3.76 ] )
			else:
				raise ValueError( 'parameters must be frequency and/or phase! Passed values are: {}'.format( parameters ) )
			x = np.arange( 0, self.n_spectrum_samples, self.delta_frequency )
			for _slice in continuities:
				axs[ index ].plot( x[ _slice ], y[ _slice ], **plot_kwargs[ index ] )
			axs[ index ].set( ylabel = y_title )
		plt.xlabel( 'Frequency [Hz]' )
		if plot_formants:
			for formant in self.formants:
				for ax in axs:
					ax.axvline( formant, color = 'gray', ls = '--' )
		for ax in axs:
			ax.label_outer()
		finalize_plot( figure, axs, **kwargs )
		return axs
#---------------------------------------------------------------------------------------------------------------------------------------------------#