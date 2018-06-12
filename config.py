#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Configuration (Global variables)
'''

SUBJECT_NUM = 40
VIDEO_NUM = 16
SAMPLE_RATE = 128.
MISSING_DATA_SUBJECT = [9, 12, 21, 22, 23, 24, 33]
FEATURE_NAMES = ['theta_power_AF3', 'theta_power_F7', 'theta_power_F3', 'theta_power_FC5', 'theta_power_T7', 'theta_power_P7', 'theta_power_O1', 'theta_power_O2', 'theta_power_P8', 'theta_power_T8', 'theta_power_FC6', 'theta_power_F4', 'theta_power_F8', 'theta_power_AF4', 'slow_alpha_power_AF3', 'slow_alpha_power_F7', 'slow_alpha_power_F3', 'slow_alpha_power_FC5', 'slow_alpha_power_T7', 'slow_alpha_power_P7', 'slow_alpha_power_O1', 'slow_alpha_power_O2', 'slow_alpha_power_P8', 'slow_alpha_power_T8', 'slow_alpha_power_FC6', 'slow_alpha_power_F4', 'slow_alpha_power_F8', 'slow_alpha_power_AF4', 'alpha_power_AF3', 'alpha_power_F7', 'alpha_power_F3', 'alpha_power_FC5', 'alpha_power_T7', 'alpha_power_P7', 'alpha_power_O1', 'alpha_power_O2', 'alpha_power_P8', 'alpha_power_T8', 'alpha_power_FC6', 'alpha_power_F4', 'alpha_power_F8', 'alpha_power_AF4', 'beta_power_AF3', 'beta_power_F7', 'beta_power_F3', 'beta_power_FC5', 'beta_power_T7', 'beta_power_P7', 'beta_power_O1', 'beta_power_O2', 'beta_power_P8', 'beta_power_T8', 'beta_power_FC6', 'beta_power_F4', 'beta_power_F8', 'beta_power_AF4', 'gamma_power_AF3', 'gamma_power_F7', 'gamma_power_F3', 'gamma_power_FC5', 'gamma_power_T7', 'gamma_power_P7', 'gamma_power_O1', 'gamma_power_O2', 'gamma_power_P8', 'gamma_power_T8', 'gamma_power_FC6', 'gamma_power_F4', 'gamma_power_F8', 'gamma_power_AF4', 'theta_spa_AF3_AF4', 'theta_spa_F7_F8', 'theta_spa_F3_F4', 'theta_spa_FC5_FC6', 'theta_spa_T7_T8', 'theta_spa_P7_P8', 'theta_spa_O1_O2', 'slow_alpha_spa_AF3_AF4', 'slow_alpha_spa_F7_F8', 'slow_alpha_spa_F3_F4', 'slow_alpha_spa_FC5_FC6', 'slow_alpha_spa_T7_T8', 'slow_alpha_spa_P7_P8', 'slow_alpha_spa_O1_O2', 'alpha_spa_AF3_AF4', 'alpha_spa_F7_F8', 'alpha_spa_F3_F4', 'alpha_spa_FC5_FC6', 'alpha_spa_T7_T8', 'alpha_spa_P7_P8', 'alpha_spa_O1_O2', 'beta_spa_AF3_AF4', 'beta_spa_F7_F8', 'beta_spa_F3_F4', 'beta_spa_FC5_FC6', 'beta_spa_T7_T8', 'beta_spa_P7_P8', 'beta_spa_O1_O2', 'gamma_spa_AF3_AF4', 'gamma_spa_F7_F8', 'gamma_spa_F3_F4', 'gamma_spa_FC5_FC6', 'gamma_spa_T7_T8', 'gamma_spa_P7_P8', 'gamma_spa_O1_O2', 'theta_relative_power_AF3', 'theta_relative_power_F7', 'theta_relative_power_F3', 'theta_relative_power_FC5', 'theta_relative_power_T7', 'theta_relative_power_P7', 'theta_relative_power_O1', 'theta_relative_power_O2', 'theta_relative_power_P8', 'theta_relative_power_T8', 'theta_relative_power_FC6', 'theta_relative_power_F4', 'theta_relative_power_F8', 'theta_relative_power_AF4', 'slow_alpha_relative_power_AF3', 'slow_alpha_relative_power_F7', 'slow_alpha_relative_power_F3', 'slow_alpha_relative_power_FC5', 'slow_alpha_relative_power_T7', 'slow_alpha_relative_power_P7', 'slow_alpha_relative_power_O1', 'slow_alpha_relative_power_O2', 'slow_alpha_relative_power_P8', 'slow_alpha_relative_power_T8', 'slow_alpha_relative_power_FC6', 'slow_alpha_relative_power_F4', 'slow_alpha_relative_power_F8', 'slow_alpha_relative_power_AF4', 'alpha_relative_power_AF3', 'alpha_relative_power_F7', 'alpha_relative_power_F3', 'alpha_relative_power_FC5', 'alpha_relative_power_T7', 'alpha_relative_power_P7', 'alpha_relative_power_O1', 'alpha_relative_power_O2', 'alpha_relative_power_P8', 'alpha_relative_power_T8', 'alpha_relative_power_FC6', 'alpha_relative_power_F4', 'alpha_relative_power_F8', 'alpha_relative_power_AF4', 'beta_relative_power_AF3', 'beta_relative_power_F7', 'beta_relative_power_F3', 'beta_relative_power_FC5', 'beta_relative_power_T7', 'beta_relative_power_P7', 'beta_relative_power_O1', 'beta_relative_power_O2', 'beta_relative_power_P8', 'beta_relative_power_T8', 'beta_relative_power_FC6', 'beta_relative_power_F4', 'beta_relative_power_F8', 'beta_relative_power_AF4', 'gamma_relative_power_AF3', 'gamma_relative_power_F7', 'gamma_relative_power_F3', 'gamma_relative_power_FC5', 'gamma_relative_power_T7', 'gamma_relative_power_P7', 'gamma_relative_power_O1', 'gamma_relative_power_O2', 'gamma_relative_power_P8', 'gamma_relative_power_T8', 'gamma_relative_power_FC6', 'gamma_relative_power_F4', 'gamma_relative_power_F8', 'gamma_relative_power_AF4', 'rms_IBI', 'mean_IBI', 'power_0.0_0.1', 'power_0.1_0.2', 'power_0.2_0.3', 'power_0.3_0.4', 'power_0.4_0.5', 'power_0.5_0.6', 'power_0.6_0.7', 'power_0.7_0.8', 'power_0.8_0.9', 'power_0.9_1.0', 'power_1.0_1.1', 'power_1.1_1.2', 'power_1.2_1.3', 'power_1.3_1.4', 'power_1.4_1.5', 'power_1.5_1.6', 'power_1.6_1.7', 'power_1.7_1.8', 'power_1.8_1.9', 'power_1.9_2.0', 'power_2.0_2.1', 'power_2.1_2.2', 'power_2.2_2.3', 'power_2.3_2.4', 'power_2.4_2.5', 'power_2.5_2.6', 'power_2.6_2.7', 'power_2.7_2.8', 'power_2.8_2.9', 'power_2.9_3.0', 'power_3.0_3.1', 'power_3.1_3.2', 'power_3.2_3.3', 'power_3.3_3.4', 'power_3.4_3.5', 'power_3.5_3.6', 'power_3.6_3.7', 'power_3.7_3.8', 'power_3.8_3.9', 'power_3.9_4.0', 'power_4.0_4.1', 'power_4.1_4.2', 'power_4.2_4.3', 'power_4.3_4.4', 'power_4.4_4.5', 'power_4.5_4.6', 'power_4.6_4.7', 'power_4.7_4.8', 'power_4.8_4.9', 'power_4.9_5.0', 'power_5.0_5.1', 'power_5.1_5.2', 'power_5.2_5.3', 'power_5.3_5.4', 'power_5.4_5.5', 'power_5.5_5.6', 'power_5.6_5.7', 'power_5.7_5.8', 'power_5.8_5.9', 'power_5.9_6.0', 'power_0.00_0.04', 'power_0.04_0.15', 'power_0.15_0.40', 'mean_heart_rate', 'std_heart_rate', 'skew_heart_rate', 'kurt_heart_rate', 'per_above_heart_rate', 'per_below_heart_rate', 'std_IBI', 'skew_IBI', 'kurt_IBI', 'per_above_IBI', 'per_below_IBI', 'LF_HF', 'LF_TF', 'HF_TF', 'nLF', 'nHF', 'mean_sr', 'mean_der_sr', 'mean_der_neg', 'pro_neg_der', 'num_local_min', 'avg_rising_time', 'power_0.00_0.11', 'power_0.11_0.23', 'power_0.23_0.34', 'power_0.34_0.46', 'power_0.46_0.57', 'power_0.57_0.69', 'power_0.69_0.80', 'power_0.80_0.91', 'power_0.91_1.03', 'power_1.03_1.14', 'power_1.14_1.26', 'power_1.26_1.37', 'power_1.37_1.49', 'power_1.49_1.60', 'power_1.60_1.71', 'power_1.71_1.83', 'power_1.83_1.94', 'power_1.94_2.06', 'power_2.06_2.17', 'power_2.17_2.29', 'power_2.29_2.40', 'zcr_SCSR', 'zcr_SCVSR', 'mean_peak_SCSR', 'mean_peak_SCVSR']
A_FEATURE_NAMES = ['ecg_rcmse_m0_s2','ecg_rcmse_m1_s2','gsr_rcmse_7','gsr_rcmse_8','gsr_rcmse_9','gsr_rcmse_10','gsr_rcmse_11','gsr_rcmse_12','gsr_rcmse_13','gsr_rcmse_14','gsr_rcmse_15','gsr_rcmse_16','gsr_rcmse_17','gsr_rcmse_18','gsr_rcmse_19','gsr_rcmse_20', 'eeg_mmpe_s18_d2_r3', 'eeg_mmpe_s19_d4_r1', 'eeg_mmpe_s11_d2_r4', 'ecg_rcmpe_s2_d3', 'ecg_rcmpe_s1_d3', 'gsr_rcmpe_s20_d2', 'gsr_rcmpe_s19_d2', 'gsr_rcmpe_s18_d2', 'gsr_rcmpe_s17_d2', 'gsr_rcmpe_s16_d2', 'gsr_rcmpe_s15_d2', 'gsr_rcmpe_s14_d2', 'gsr_rcmpe_s13_d2', 'gsr_rcmpe_s12_d2', 'gsr_rcmpe_s11_d2', 'gsr_rcmpe_s10_d2', 'gsr_rcmpe_s9_d2', 'gsr_rcmpe_s8_d2', 'gsr_rcmpe_s7_d2', 'gsr_rcmpe_s6_d2', 'gsr_rcmpe_s1_d2', 'gsr_rcmpe_s5_d2', 'gsr_rcmpe_s4_d2', 'gsr_rcmpe_s3_d2', 'gsr_rcmpe_s1_d3']
V_FEATURE_NAMES = ['ecg_rcmse_m0_s2','ecg_rcmse_m1_s2','ecg_rcmse_m2a_s2','ecg_rcmse_m0_s3', 'eeg_mmpe_s17_d6_r2', 'eeg_mmpe_s20_d6_r2', 'eeg_mmpe_s20_d6_r4', 'eeg_mmpe_s18_d6_r5', 'eeg_mmpe_s14_d6_r2', 'eeg_mmpe_s15_d6_r2', 'eeg_mmpe_s18_d6_r2', 'eeg_mmpe_s18_d6_r3', 'eeg_mmpe_s17_d6_r3', 'eeg_mmpe_s15_d6_r5', 'eeg_mmpe_s14_d6_r3', 'eeg_mmpe_s20_d6_r1', 'eeg_mmpe_s16_d6_r2', 'eeg_mmpe_s16_d6_r5', 'eeg_mmpe_s16_d6_r3', 'eeg_mmpe_s18_d6_r1', 'eeg_mmpe_s14_d6_r5', 'eeg_mmpe_s15_d6_r3', 'eeg_mmpe_s13_d6_r3', 'eeg_mmpe_s13_d6_r2', 'eeg_mmpe_s20_d6_r5', 'eeg_mmpe_s17_d6_r5', 'eeg_mmpe_s12_d6_r2', 'eeg_mmpe_s19_d6_r5','eeg_mmpe_s19_d6_r2', 'eeg_mmpe_s16_d6_r1', 'eeg_mmpe_s20_d6_r3', 'eeg_mmpe_s17_d6_r4', 'eeg_mmpe_s19_d6_r4', 'eeg_mmpe_s18_d6_r4', 'eeg_mmpe_s19_d6_r1', 'eeg_mmpe_s17_d6_r1', 'eeg_mmpe_s11_d6_r2', 'eeg_mmpe_s16_d6_r4', 'eeg_mmpe_s19_d6_r3', 'eeg_mmpe_s15_d6_r4', 'eeg_mmpe_s12_d6_r3', 'eeg_mmpe_s13_d6_r5', 'eeg_mmpe_s14_d6_r4', 'eeg_mmpe_s15_d6_r1', 'eeg_mmpe_s20_d2_r2', 'eeg_mmpe_s17_d5_r3', 'eeg_mmpe_s14_d6_r1', 'eeg_mmpe_s10_d6_r2', 'eeg_mmpe_s13_d6_r4', 'eeg_mmpe_s11_d6_r3', 'eeg_mmpe_s18_d5_r3', 'eeg_mmpe_s16_d5_r5', 'eeg_mmpe_s18_d3_r2', 'eeg_mmpe_s20_d5_r1', 'eeg_mmpe_s18_d5_r2', 'eeg_mmpe_s18_d2_r2', 'eeg_mmpe_s18_d5_r5', 'eeg_mmpe_s12_d6_r5', 'eeg_mmpe_s17_d5_r2', 'eeg_mmpe_s11_d6_r5', 'eeg_mmpe_s18_d3_r3', 'eeg_mmpe_s12_d6_r4', 'eeg_mmpe_s9_d6_r2', 'eeg_mmpe_s16_d5_r3', 'eeg_mmpe_s15_d5_r3', 'eeg_mmpe_s16_d5_r2', 'eeg_mmpe_s18_d5_r1', 'eeg_mmpe_s15_d5_r5', 'eeg_mmpe_s20_d5_r4', 'eeg_mmpe_s11_d6_r4', 'eeg_mmpe_s17_d5_r5', 'eeg_mmpe_s13_d6_r1', 'eeg_mmpe_s19_d5_r4', 'eeg_mmpe_s18_d4_r3', 'eeg_mmpe_s15_d5_r2', 'eeg_mmpe_s14_d5_r2', 'eeg_mmpe_s8_d6_r2', 'eeg_mmpe_s19_d5_r1', 'eeg_mmpe_s20_d5_r2', 'eeg_mmpe_s12_d6_r1', 'eeg_mmpe_s10_d6_r3', 'eeg_mmpe_s18_d4_r2', 'eeg_mmpe_s16_d2_r4', 'eeg_mmpe_s14_d5_r3', 'eeg_mmpe_s16_d4_r5', 'eeg_mmpe_s17_d3_r3', 'eeg_mmpe_s10_d6_r4', 'eeg_mmpe_s17_d4_r3', 'eeg_mmpe_s14_d5_r5', 'eeg_mmpe_s13_d2_r4', 'eeg_mmpe_s17_d5_r1', 'eeg_mmpe_s7_d6_r2', 'eeg_mmpe_s19_d5_r3', 'ecg_rcmpe_s2_d6', 'ecg_rcmpe_s3_d6', 'ecg_rcmpe_s1_d6', 'ecg_rcmpe_s2_d5', 'ecg_rcmpe_s1_d5', 'ecg_rcmpe_s3_d5', 'ecg_rcmpe_s2_d4', 'ecg_rcmpe_s3_d4']
