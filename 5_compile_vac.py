# This script uses all the fits files we have generated and compile VAC

import os
import numpy as np
from astropy.io import fits

from config import allstar_path, gaia_rowmatch_f, astronn_chem_f, astronn_dist_f, galpy_orbitparams_f, \
    astronn_ages_f, astronn_apogee_vac_f

if os.path.exists(astronn_apogee_vac_f):
    raise FileExistsError(f"{astronn_apogee_vac_f} already existed")

allstar_data = fits.getdata(allstar_path)
f_gaia = fits.getdata(gaia_rowmatch_f)

f_chem = fits.getdata(astronn_chem_f)
f_dist = fits.getdata(astronn_dist_f)
f_ages = fits.getdata(astronn_ages_f)
f_orbitparams = fits.getdata(galpy_orbitparams_f)

c = [fits.Column(name='APOGEE_ID', array=allstar_data['APOGEE_ID'], format="18A"),
     fits.Column(name='LOCATION_ID', array=allstar_data['LOCATION_ID'], format="J"),
     fits.Column(name='TELESCOPE', array=allstar_data['TELESCOPE'], format="8A"),
     fits.Column(name='RA_APOGEE', array=allstar_data['RA'], format='D'),
     fits.Column(name='DEC_APOGEE', array=allstar_data['DEC'], format='D'),
     fits.Column(name='TEFF', array=f_chem['astroNN'][:, 0], format='E'),
     fits.Column(name='TEFF_ERR', array=f_chem['astroNN_error'][:, 0], format='E'),
     fits.Column(name='LOGG', array=f_chem['astroNN'][:, 1], format='E'),
     fits.Column(name='LOGG_ERR', array=f_chem['astroNN_error'][:, 1], format='E'),
     fits.Column(name='C_H', array=f_chem['astroNN'][:, 2], format='E'),
     fits.Column(name='C_H_ERR', array=f_chem['astroNN_error'][:, 2], format='E'),
     fits.Column(name='CI_H', array=f_chem['astroNN'][:, 3], format='E'),
     fits.Column(name='CI_H_ERR', array=f_chem['astroNN_error'][:, 3], format='E'),
     fits.Column(name='N_H', array=f_chem['astroNN'][:, 4], format='E'),
     fits.Column(name='N_H_ERR', array=f_chem['astroNN_error'][:, 4], format='E'),
     fits.Column(name='O_H', array=f_chem['astroNN'][:, 5], format='E'),
     fits.Column(name='O_H_ERR', array=f_chem['astroNN_error'][:, 5], format='E'),
     fits.Column(name='NA_H', array=f_chem['astroNN'][:, 6], format='E'),
     fits.Column(name='NA_H_ERR', array=f_chem['astroNN_error'][:, 6], format='E'),
     fits.Column(name='MG_H', array=f_chem['astroNN'][:, 7], format='E'),
     fits.Column(name='MG_H_ERR', array=f_chem['astroNN_error'][:, 7], format='E'),
     fits.Column(name='AL_H', array=f_chem['astroNN'][:, 8], format='E'),
     fits.Column(name='AL_H_ERR', array=f_chem['astroNN_error'][:, 8], format='E'),
     fits.Column(name='SI_H', array=f_chem['astroNN'][:, 9], format='E'),
     fits.Column(name='SI_H_ERR', array=f_chem['astroNN_error'][:, 9], format='E'),
     fits.Column(name='P_H', array=f_chem['astroNN'][:, 10], format='E'),
     fits.Column(name='P_H_ERR', array=f_chem['astroNN_error'][:, 10], format='E'),
     fits.Column(name='S_H', array=f_chem['astroNN'][:, 11], format='E'),
     fits.Column(name='S_H_ERR', array=f_chem['astroNN_error'][:, 11], format='E'),
     fits.Column(name='K_H', array=f_chem['astroNN'][:, 12], format='E'),
     fits.Column(name='K_H_ERR', array=f_chem['astroNN_error'][:, 12], format='E'),
     fits.Column(name='CA_H', array=f_chem['astroNN'][:, 13], format='E'),
     fits.Column(name='CA_H_ERR', array=f_chem['astroNN_error'][:, 13], format='E'),
     fits.Column(name='TI_H', array=f_chem['astroNN'][:, 14], format='E'),
     fits.Column(name='TI_H_ERR', array=f_chem['astroNN_error'][:, 14], format='E'),
     fits.Column(name='TIII_H', array=f_chem['astroNN'][:, 15], format='E'),
     fits.Column(name='TIII_H_ERR', array=f_chem['astroNN_error'][:, 15], format='E'),
     fits.Column(name='V_H', array=f_chem['astroNN'][:, 16], format='E'),
     fits.Column(name='V_H_ERR', array=f_chem['astroNN_error'][:, 16], format='E'),
     fits.Column(name='CR_H', array=f_chem['astroNN'][:, 17], format='E'),
     fits.Column(name='CR_H_ERR', array=f_chem['astroNN_error'][:, 17], format='E'),
     fits.Column(name='MN_H', array=f_chem['astroNN'][:, 18], format='E'),
     fits.Column(name='MN_H_ERR', array=f_chem['astroNN_error'][:, 18], format='E'),
     fits.Column(name='FE_H', array=f_chem['astroNN'][:, 19], format='E'),
     fits.Column(name='FE_H_ERR', array=f_chem['astroNN_error'][:, 19], format='E'),
     fits.Column(name='CO_H', array=f_chem['astroNN'][:, 20], format='E'),
     fits.Column(name='CO_H_ERR', array=f_chem['astroNN_error'][:, 20], format='E'),
     fits.Column(name='NI_H', array=f_chem['astroNN'][:, 21], format='E'),
     fits.Column(name='NI_H_ERR', array=f_chem['astroNN_error'][:, 21], format='E'),
     fits.Column(name='dist', array=f_dist['dist'], format='D'),
     fits.Column(name='dist_error', array=f_dist['dist_error'], format='D'),
     fits.Column(name='dist_model_error', array=f_dist['dist_model_error'], format='D'),
     fits.Column(name='nn_parallax', array=f_dist['nn_parallax'], format='D'),
     fits.Column(name='nn_parallax_error', array=f_dist['nn_parallax_error'], format='D'),
     fits.Column(name='nn_parallax_model_error', array=f_dist['nn_parallax_model_error'], format='D'),
     fits.Column(name='fakemag', array=f_dist['fakemag'], format='D'),
     fits.Column(name='fakemag_error', array=f_dist['fakemag_error'], format='D'),
     fits.Column(name='weighted_dist', array=f_dist['weighted_dist'], format='D'),
     fits.Column(name='weighted_dist_error', array=f_dist['weighted_dist_error'], format='D'),
     fits.Column(name='RA', array=f_gaia['RA'], format='D'),
     fits.Column(name='DEC', array=f_gaia['DEC'], format='D'),
     fits.Column(name='pmra', array=f_gaia['pmra'], format='D'),
     fits.Column(name='pmra_error', array=f_gaia['pmra_error'], format='D'),
     fits.Column(name='ref_epoch', array=f_gaia['ref_epoch'], format='D'),  # new in DR3
    #  fits.Column(name='dr2_source_id', array=f_gaia['dr2_source_id'], format='K'),  # new in DR3
     fits.Column(name='pmdec', array=f_gaia['pmdec'], format='D'),
     fits.Column(name='pmdec_error', array=f_gaia['pmdec_error'], format='D'),
     fits.Column(name='phot_g_mean_mag', array=f_gaia['phot_g_mean_mag'], format='D'),
     fits.Column(name='bp_rp', array=f_gaia['bp_rp'], format='D'),
     fits.Column(name='g_rp', array=f_gaia['g_rp'], format='D'),  # new in DR3
     fits.Column(name='VHELIO_AVG', array=allstar_data['VHELIO_AVG'], format='E'),

     fits.Column(name='age', array=f_ages['age'], format='D'),
     fits.Column(name='age_linear_correct', array=f_ages['age_linear_correct'], format='D'),
     fits.Column(name='age_lowess_correct', array=f_ages['age_lowess_correct'], format='D'),
     fits.Column(name='age_total_error', array=f_ages['age_total_error'], format='D'),
     fits.Column(name='age_model_error', array=f_ages['age_model_error'], format='D'),
     fits.Column(name='source_id', array=f_gaia['source_id'], format='K'),

     fits.Column(name='galr', array=f_orbitparams['galr'], format='D'),
     fits.Column(name='galphi', array=f_orbitparams['galphi'], format='D'),
     fits.Column(name='galz', array=f_orbitparams['galz'], format='D'),
     fits.Column(name='galvr', array=f_orbitparams['galvr'], format='D'),
     fits.Column(name='galvt', array=f_orbitparams['galvt'], format='D'),
     fits.Column(name='galvz', array=f_orbitparams['galvz'], format='D'),
     fits.Column(name='galr_err', array=f_orbitparams['galr_err'], format='D'),
     fits.Column(name='galphi_err', array=f_orbitparams['galphi_err'], format='D'),
     fits.Column(name='galz_err', array=f_orbitparams['galz_err'], format='D'),
     fits.Column(name='galvr_err', array=f_orbitparams['galvr_err'], format='D'),
     fits.Column(name='galvt_err', array=f_orbitparams['galvt_err'], format='D'),
     fits.Column(name='galvz_err', array=f_orbitparams['galvz_err'], format='D'),
     fits.Column(name='galvr_galvt_corr', array=f_orbitparams['galvr_galvt_corr'], format='D'),
     fits.Column(name='galvr_galvz_corr', array=f_orbitparams['galvr_galvz_corr'], format='D'),
     fits.Column(name='galvt_galvz_corr', array=f_orbitparams['galvt_galvz_corr'], format='D'),

     fits.Column(name='e', array=f_orbitparams['e'], format='D'),
     fits.Column(name='e_err', array=f_orbitparams['e_err'], format='D'),
     fits.Column(name='zmax', array=f_orbitparams['zmax'], format='D'),
     fits.Column(name='zmax_err', array=f_orbitparams['zmax_err'], format='D'),
     fits.Column(name='rperi', array=f_orbitparams['rperi'], format='D'),
     fits.Column(name='rperi_err', array=f_orbitparams['rperi_err'], format='D'),
     fits.Column(name='rap', array=f_orbitparams['rap'], format='D'),
     fits.Column(name='rap_err', array=f_orbitparams['rap_err'], format='D'),
     fits.Column(name='e_zmax_corr', array=f_orbitparams['e_zmax_corr'], format='D'),
     fits.Column(name='e_rperi_corr', array=f_orbitparams['e_rperi_corr'], format='D'),
     fits.Column(name='e_rap_corr', array=f_orbitparams['e_rap_corr'], format='D'),
     fits.Column(name='zmax_rperi_corr', array=f_orbitparams['zmax_rperi_corr'], format='D'),
     fits.Column(name='zmax_rap_corr', array=f_orbitparams['zmax_rperi_corr'], format='D'),
     fits.Column(name='rperi_rap_corr', array=f_orbitparams['rperi_rap_corr'], format='D'),
     fits.Column(name='jr', array=f_orbitparams['jr'], format='D'),
     fits.Column(name='jr_err', array=f_orbitparams['jr_err'], format='D'),
     fits.Column(name='Lz', array=f_orbitparams['Lz'], format='D'),
     fits.Column(name='Lz_err', array=f_orbitparams['Lz_err'], format='D'),
     fits.Column(name='jz', array=f_orbitparams['jz'], format='D'),
     fits.Column(name='jz_err', array=f_orbitparams['jz_err'], format='D'),
     fits.Column(name='jr_Lz_corr', array=f_orbitparams['jr_Lz_corr'], format='D'),
     fits.Column(name='jr_jz_corr', array=f_orbitparams['jr_jz_corr'], format='D'),
     fits.Column(name='lz_jz_corr', array=f_orbitparams['lz_jz_corr'], format='D'),
     fits.Column(name='omega_r', array=f_orbitparams['omega_r'], format='D'),
     fits.Column(name='omega_r_err', array=f_orbitparams['omega_r_err'], format='D'),
     fits.Column(name='omega_phi', array=f_orbitparams['omega_phi'], format='D'),
     fits.Column(name='omega_phi_err', array=f_orbitparams['omega_phi_err'], format='D'),
     fits.Column(name='omega_z', array=f_orbitparams['omega_z'], format='D'),
     fits.Column(name='omega_z_err', array=f_orbitparams['omega_z_err'], format='D'),
     fits.Column(name='theta_r', array=f_orbitparams['theta_r'], format='D'),
     fits.Column(name='theta_r_err', array=f_orbitparams['theta_r_err'], format='D'),
     fits.Column(name='theta_phi', array=f_orbitparams['theta_phi'], format='D'),
     fits.Column(name='theta_phi_err', array=f_orbitparams['theta_phi_err'], format='D'),
     fits.Column(name='theta_z', array=f_orbitparams['theta_z'], format='D'),
     fits.Column(name='theta_z_err', array=f_orbitparams['theta_z_err'], format='D'),
     fits.Column(name='rl', array=f_orbitparams['rl'], format='D'),
     fits.Column(name='rl_err', array=f_orbitparams['rl_err'], format='D'),
     fits.Column(name='Energy', array=f_orbitparams['Energy'], format='D'),
     fits.Column(name='Energy_err', array=f_orbitparams['Energy_err'], format='D'),
     fits.Column(name='EminusEc', array=f_orbitparams['EminusEc'], format='D'),
     fits.Column(name='EminusEc_err', array=f_orbitparams['EminusEc_err'], format='D')]

for ci in c:
    try:
        assert np.all(ci.array!=-9999.)
    except TypeError:
        pass
    except AssertionError:
        print(ci)

# save a fits
t = fits.BinTableHDU.from_columns(c)
t.writeto(astronn_apogee_vac_f)
