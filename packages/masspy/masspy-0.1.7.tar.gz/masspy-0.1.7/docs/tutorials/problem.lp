\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
 
Subject To
 glc__D_c: - HEX1 + HEX1_reverse_25efa + SK_glc__D_c
   - SK_glc__D_c_reverse_e1695 = 0
 g6p_c: HEX1 - HEX1_reverse_25efa - PGI + PGI_reverse_27efc - G6PDH2r
   + G6PDH2r_reverse_19ddf = 0
 f6p_c: PGI - PGI_reverse_27efc + TKT2 - TKT2_reverse_7ebc7 + TALA
   - TALA_reverse_adfda - PFK_R02 + PFK_R02_reverse_031bc - PFK_R12
   + PFK_R12_reverse_a500a - PFK_R22 + PFK_R22_reverse_37f36 - PFK_R32
   + PFK_R32_reverse_e6e63 - PFK_R42 + PFK_R42_reverse_3dab0 = 0
 fdp_c: - FBA + FBA_reverse_84806 + PFK_R03 - PFK_R03_reverse_3d3dc
   + PFK_R13 - PFK_R13_reverse_0e2de + PFK_R23 - PFK_R23_reverse_e55ae
   + PFK_R33 - PFK_R33_reverse_fbc5d + PFK_R43 - PFK_R43_reverse_58b16 = 0
 dhap_c: FBA - FBA_reverse_84806 - TPI + TPI_reverse_c2c3b = 0
 g3p_c: FBA - FBA_reverse_84806 + TPI - TPI_reverse_c2c3b - GAPD
   + GAPD_reverse_459c1 + TKT1 - TKT1_reverse_a1021 + TKT2
   - TKT2_reverse_7ebc7 - TALA + TALA_reverse_adfda = 0
 _13dpg_c: GAPD - GAPD_reverse_459c1 - PGK + PGK_reverse_02696 - DPGM
   + DPGM_reverse_f8976 = 0
 _3pg_c: PGK - PGK_reverse_02696 - PGM + PGM_reverse_fc9af + DPGase
   - DPGase_reverse_3b298 = 0
 _2pg_c: PGM - PGM_reverse_fc9af - ENO + ENO_reverse_40eea = 0
 pep_c: ENO - ENO_reverse_40eea - PYK + PYK_reverse_bc8ff = 0
 pyr_c: PYK - PYK_reverse_bc8ff - LDH_L + LDH_L_reverse_fa844 - SK_pyr_c
   + SK_pyr_c_reverse_091f2 = 0
 lac__L_c: LDH_L - LDH_L_reverse_fa844 - SK_lac__L_c
   + SK_lac__L_c_reverse_c0bd6 = 0
 _6pgl_c: G6PDH2r - G6PDH2r_reverse_19ddf - PGL + PGL_reverse_2bb6b = 0
 _6pgc_c: PGL - PGL_reverse_2bb6b - GND + GND_reverse_eec5c = 0
 ru5p__D_c: GND - GND_reverse_eec5c - RPE + RPE_reverse_a1b04 - RPI
   + RPI_reverse_853a1 = 0
 xu5p__D_c: RPE - RPE_reverse_a1b04 - TKT1 + TKT1_reverse_a1021 - TKT2
   + TKT2_reverse_7ebc7 = 0
 r5p_c: RPI - RPI_reverse_853a1 - TKT1 + TKT1_reverse_a1021 + PPM
   - PPM_reverse_4bb1e - PRPPS + PRPPS_reverse_dd7f2 = 0
 s7p_c: TKT1 - TKT1_reverse_a1021 - TALA + TALA_reverse_adfda = 0
 e4p_c: - TKT2 + TKT2_reverse_7ebc7 + TALA - TALA_reverse_adfda = 0
 ade_c: - ADPT + ADPT_reverse_567cf - SK_ade_c + SK_ade_c_reverse_c815c
   = 0
 adn_c: - ADNK1 + ADNK1_reverse_fe466 + NTD7 - NTD7_reverse_20dab - ADA
   + ADA_reverse_347cb - SK_adn_c + SK_adn_c_reverse_74eb8 = 0
 imp_c: AMPDA - AMPDA_reverse_7544e - NTD11 + NTD11_reverse_39abf = 0
 ins_c: ADA - ADA_reverse_347cb + NTD11 - NTD11_reverse_39abf - PUNP5
   + PUNP5_reverse_e49fe - SK_ins_c + SK_ins_c_reverse_d9db6 = 0
 hxan_c: PUNP5 - PUNP5_reverse_e49fe - SK_hxan_c + SK_hxan_c_reverse_455ab
   = 0
 r1p_c: PUNP5 - PUNP5_reverse_e49fe - PPM + PPM_reverse_4bb1e = 0
 prpp_c: PRPPS - PRPPS_reverse_dd7f2 - ADPT + ADPT_reverse_567cf = 0
 _23dpg_c: DPGM - DPGM_reverse_f8976 - DPGase + DPGase_reverse_3b298
   - HBDPG + HBDPG_reverse_c574e = 0
 hb_c: - HBDPG + HBDPG_reverse_c574e - HBO1 + HBO1_reverse_485f4 = 0
 hb_1o2_c: HBO1 - HBO1_reverse_485f4 - HBO2 + HBO2_reverse_67566 = 0
 hb_2o2_c: HBO2 - HBO2_reverse_67566 - HBO3 + HBO3_reverse_5cd11 = 0
 hb_3o2_c: HBO3 - HBO3_reverse_5cd11 - HBO4 + HBO4_reverse_4a041 = 0
 hb_4o2_c: HBO4 - HBO4_reverse_4a041 = 0
 dhb_c: HBDPG - HBDPG_reverse_c574e = 0
 nad_c: - GAPD + GAPD_reverse_459c1 + LDH_L - LDH_L_reverse_fa844 + DM_nadh
   - DM_nadh_reverse_52c09 = 0
 nadh_c: GAPD - GAPD_reverse_459c1 - LDH_L + LDH_L_reverse_fa844 - DM_nadh
   + DM_nadh_reverse_52c09 = 0
 amp_c: ADNK1 - ADNK1_reverse_fe466 - NTD7 + NTD7_reverse_20dab - AMPDA
   + AMPDA_reverse_7544e + PRPPS - PRPPS_reverse_dd7f2 + ADPT
   - ADPT_reverse_567cf + ADK1 - ADK1_reverse_a6f90 - PFK_R10
   + PFK_R10_reverse_051a9 - PFK_R20 + PFK_R20_reverse_29211 - PFK_R30
   + PFK_R30_reverse_fc18f - PFK_R40 + PFK_R40_reverse_48b56 = 0
 adp_c: HEX1 - HEX1_reverse_25efa - PGK + PGK_reverse_02696 - PYK
   + PYK_reverse_bc8ff + ADNK1 - ADNK1_reverse_fe466 - 2 ADK1
   + 2 ADK1_reverse_a6f90 + ATPM - ATPM_reverse_5b752 + PFK_R03
   - PFK_R03_reverse_3d3dc + PFK_R13 - PFK_R13_reverse_0e2de + PFK_R23
   - PFK_R23_reverse_e55ae + PFK_R33 - PFK_R33_reverse_fbc5d + PFK_R43
   - PFK_R43_reverse_58b16 = 0
 atp_c: - HEX1 + HEX1_reverse_25efa + PGK - PGK_reverse_02696 + PYK
   - PYK_reverse_bc8ff - ADNK1 + ADNK1_reverse_fe466 - PRPPS
   + PRPPS_reverse_dd7f2 + ADK1 - ADK1_reverse_a6f90 - ATPM
   + ATPM_reverse_5b752 - PFK_R01 + PFK_R01_reverse_68ed9 - PFK_R11
   + PFK_R11_reverse_89adc - PFK_R21 + PFK_R21_reverse_336ca - PFK_R31
   + PFK_R31_reverse_3cee8 - PFK_R41 + PFK_R41_reverse_20e9f - PFK_T1
   + PFK_T1_reverse_2ac1a - PFK_T2 + PFK_T2_reverse_4e834 - PFK_T3
   + PFK_T3_reverse_96373 - PFK_T4 + PFK_T4_reverse_1d7d4 = 0
 nadp_c: - G6PDH2r + G6PDH2r_reverse_19ddf - GND + GND_reverse_eec5c
   + GTHOr - GTHOr_reverse_8f1f9 = 0
 nadph_c: G6PDH2r - G6PDH2r_reverse_19ddf + GND - GND_reverse_eec5c - GTHOr
   + GTHOr_reverse_8f1f9 = 0
 gthrd_c: 2 GTHOr - 2 GTHOr_reverse_8f1f9 - 2 GSHR + 2 GSHR_reverse_3d920
   = 0
 gthox_c: - GTHOr + GTHOr_reverse_8f1f9 + GSHR - GSHR_reverse_3d920 = 0
 pi_c: - GAPD + GAPD_reverse_459c1 + NTD7 - NTD7_reverse_20dab + NTD11
   - NTD11_reverse_39abf - PUNP5 + PUNP5_reverse_e49fe + 2 ADPT
   - 2 ADPT_reverse_567cf + DPGase - DPGase_reverse_3b298 + ATPM
   - ATPM_reverse_5b752 - SK_pi_c + SK_pi_c_reverse_daf23 = 0
 h_c: HEX1 - HEX1_reverse_25efa + GAPD - GAPD_reverse_459c1 - PYK
   + PYK_reverse_bc8ff - LDH_L + LDH_L_reverse_fa844 + G6PDH2r
   - G6PDH2r_reverse_19ddf + PGL - PGL_reverse_2bb6b + ADNK1
   - ADNK1_reverse_fe466 + PRPPS - PRPPS_reverse_dd7f2 + ADPT
   - ADPT_reverse_567cf + DPGM - DPGM_reverse_f8976 + ATPM
   - ATPM_reverse_5b752 + DM_nadh - DM_nadh_reverse_52c09 - GTHOr
   + GTHOr_reverse_8f1f9 + 2 GSHR - 2 GSHR_reverse_3d920 - SK_h_c
   + SK_h_c_reverse_aa945 + PFK_R03 - PFK_R03_reverse_3d3dc + PFK_R13
   - PFK_R13_reverse_0e2de + PFK_R23 - PFK_R23_reverse_e55ae + PFK_R33
   - PFK_R33_reverse_fbc5d + PFK_R43 - PFK_R43_reverse_58b16 = 0
 h2o_c: ENO - ENO_reverse_40eea - PGL + PGL_reverse_2bb6b - NTD7
   + NTD7_reverse_20dab - ADA + ADA_reverse_347cb - AMPDA
   + AMPDA_reverse_7544e - NTD11 + NTD11_reverse_39abf - ADPT
   + ADPT_reverse_567cf - DPGase + DPGase_reverse_3b298 - ATPM
   + ATPM_reverse_5b752 - SK_h2o_c + SK_h2o_c_reverse_b6e75 = 0
 co2_c: GND - GND_reverse_eec5c - SK_co2_c + SK_co2_c_reverse_b6c81 = 0
 nh3_c: ADA - ADA_reverse_347cb + AMPDA - AMPDA_reverse_7544e - SK_nh3_c
   + SK_nh3_c_reverse_959e3 = 0
 o2_c: - HBO1 + HBO1_reverse_485f4 - HBO2 + HBO2_reverse_67566 - HBO3
   + HBO3_reverse_5cd11 - HBO4 + HBO4_reverse_4a041 - SK_o2_c
   + SK_o2_c_reverse_527dc = 0
 pfk_R0_A_c: PFK_R01 - PFK_R01_reverse_68ed9 - PFK_R02
   + PFK_R02_reverse_031bc = 0
 pfk_R0_c: - PFK_R01 + PFK_R01_reverse_68ed9 + PFK_R03
   - PFK_R03_reverse_3d3dc - PFK_R10 + PFK_R10_reverse_051a9 - PFK_L
   + PFK_L_reverse_a21e0 = 0
 pfk_R0_AF_c: PFK_R02 - PFK_R02_reverse_031bc - PFK_R03
   + PFK_R03_reverse_3d3dc = 0
 pfk_R1_c: PFK_R10 - PFK_R10_reverse_051a9 - PFK_R11
   + PFK_R11_reverse_89adc + PFK_R13 - PFK_R13_reverse_0e2de - PFK_R20
   + PFK_R20_reverse_29211 = 0
 pfk_R1_A_c: PFK_R11 - PFK_R11_reverse_89adc - PFK_R12
   + PFK_R12_reverse_a500a = 0
 pfk_R1_AF_c: PFK_R12 - PFK_R12_reverse_a500a - PFK_R13
   + PFK_R13_reverse_0e2de = 0
 pfk_R2_c: PFK_R20 - PFK_R20_reverse_29211 - PFK_R21
   + PFK_R21_reverse_336ca + PFK_R23 - PFK_R23_reverse_e55ae - PFK_R30
   + PFK_R30_reverse_fc18f = 0
 pfk_R2_A_c: PFK_R21 - PFK_R21_reverse_336ca - PFK_R22
   + PFK_R22_reverse_37f36 = 0
 pfk_R2_AF_c: PFK_R22 - PFK_R22_reverse_37f36 - PFK_R23
   + PFK_R23_reverse_e55ae = 0
 pfk_R3_c: PFK_R30 - PFK_R30_reverse_fc18f - PFK_R31
   + PFK_R31_reverse_3cee8 + PFK_R33 - PFK_R33_reverse_fbc5d - PFK_R40
   + PFK_R40_reverse_48b56 = 0
 pfk_R3_A_c: PFK_R31 - PFK_R31_reverse_3cee8 - PFK_R32
   + PFK_R32_reverse_e6e63 = 0
 pfk_R3_AF_c: PFK_R32 - PFK_R32_reverse_e6e63 - PFK_R33
   + PFK_R33_reverse_fbc5d = 0
 pfk_R4_c: PFK_R40 - PFK_R40_reverse_48b56 - PFK_R41
   + PFK_R41_reverse_20e9f + PFK_R43 - PFK_R43_reverse_58b16 = 0
 pfk_R4_A_c: PFK_R41 - PFK_R41_reverse_20e9f - PFK_R42
   + PFK_R42_reverse_3dab0 = 0
 pfk_R4_AF_c: PFK_R42 - PFK_R42_reverse_3dab0 - PFK_R43
   + PFK_R43_reverse_58b16 = 0
 pfk_T0_c: PFK_L - PFK_L_reverse_a21e0 - PFK_T1 + PFK_T1_reverse_2ac1a = 0
 pfk_T1_c: PFK_T1 - PFK_T1_reverse_2ac1a - PFK_T2 + PFK_T2_reverse_4e834
   = 0
 pfk_T2_c: PFK_T2 - PFK_T2_reverse_4e834 - PFK_T3 + PFK_T3_reverse_96373
   = 0
 pfk_T3_c: PFK_T3 - PFK_T3_reverse_96373 - PFK_T4 + PFK_T4_reverse_1d7d4
   = 0
 pfk_T4_c: PFK_T4 - PFK_T4_reverse_1d7d4 = 0
Bounds
 -123 <= HEX1 <= 456
 HEX1_reverse_25efa <= 1000
 PGI <= 1000
 PGI_reverse_27efc <= 1000
 FBA <= 1000
 FBA_reverse_84806 <= 1000
 TPI <= 1000
 TPI_reverse_c2c3b <= 1000
 GAPD <= 1000
 GAPD_reverse_459c1 <= 1000
 PGK <= 1000
 PGK_reverse_02696 <= 1000
 PGM <= 1000
 PGM_reverse_fc9af <= 1000
 ENO <= 1000
 ENO_reverse_40eea <= 1000
 PYK <= 1000
 PYK_reverse_bc8ff <= 1000
 LDH_L <= 1000
 LDH_L_reverse_fa844 <= 1000
 G6PDH2r <= 1000
 G6PDH2r_reverse_19ddf <= 1000
 PGL <= 1000
 PGL_reverse_2bb6b <= 1000
 GND <= 1000
 GND_reverse_eec5c <= 1000
 RPE <= 1000
 RPE_reverse_a1b04 <= 1000
 RPI <= 1000
 RPI_reverse_853a1 <= 1000
 TKT1 <= 1000
 TKT1_reverse_a1021 <= 1000
 TKT2 <= 1000
 TKT2_reverse_7ebc7 <= 1000
 TALA <= 1000
 TALA_reverse_adfda <= 1000
 ADNK1 <= 1000
 ADNK1_reverse_fe466 <= 1000
 NTD7 <= 1000
 NTD7_reverse_20dab <= 1000
 ADA <= 1000
 ADA_reverse_347cb <= 1000
 AMPDA <= 1000
 AMPDA_reverse_7544e <= 1000
 NTD11 <= 1000
 NTD11_reverse_39abf <= 1000
 PUNP5 <= 1000
 PUNP5_reverse_e49fe <= 1000
 PPM <= 1000
 PPM_reverse_4bb1e <= 1000
 PRPPS <= 1000
 PRPPS_reverse_dd7f2 <= 1000
 ADPT <= 1000
 ADPT_reverse_567cf <= 1000
 ADK1 <= 1000
 ADK1_reverse_a6f90 <= 1000
 DPGM <= 1000
 DPGM_reverse_f8976 <= 1000
 DPGase <= 1000
 DPGase_reverse_3b298 <= 1000
 HBDPG <= 1000
 HBDPG_reverse_c574e <= 1000
 HBO1 <= 1000
 HBO1_reverse_485f4 <= 1000
 HBO2 <= 1000
 HBO2_reverse_67566 <= 1000
 HBO3 <= 1000
 HBO3_reverse_5cd11 <= 1000
 HBO4 <= 1000
 HBO4_reverse_4a041 <= 1000
 ATPM <= 1000
 ATPM_reverse_5b752 <= 1000
 DM_nadh <= 1000
 DM_nadh_reverse_52c09 <= 1000
 GTHOr <= 1000
 GTHOr_reverse_8f1f9 <= 1000
 GSHR <= 1000
 GSHR_reverse_3d920 <= 1000
 SK_glc__D_c <= 1000
 SK_glc__D_c_reverse_e1695 <= 1000
 SK_pyr_c <= 1000
 SK_pyr_c_reverse_091f2 <= 1000
 SK_lac__L_c <= 1000
 SK_lac__L_c_reverse_c0bd6 <= 1000
 SK_ade_c <= 1000
 SK_ade_c_reverse_c815c <= 1000
 SK_adn_c <= 1000
 SK_adn_c_reverse_74eb8 <= 1000
 SK_ins_c <= 1000
 SK_ins_c_reverse_d9db6 <= 1000
 SK_hxan_c <= 1000
 SK_hxan_c_reverse_455ab <= 1000
 SK_pi_c <= 1000
 SK_pi_c_reverse_daf23 <= 1000
 SK_h_c <= 1000
 SK_h_c_reverse_aa945 <= 1000
 SK_h2o_c <= 1000
 SK_h2o_c_reverse_b6e75 <= 1000
 SK_co2_c <= 1000
 SK_co2_c_reverse_b6c81 <= 1000
 SK_nh3_c <= 1000
 SK_nh3_c_reverse_959e3 <= 1000
 SK_o2_c <= 1000
 SK_o2_c_reverse_527dc <= 1000
 PFK_R01 <= 1000
 PFK_R01_reverse_68ed9 <= 1000
 PFK_R02 <= 1000
 PFK_R02_reverse_031bc <= 1000
 PFK_R03 <= 1000
 PFK_R03_reverse_3d3dc <= 1000
 PFK_R10 <= 1000
 PFK_R10_reverse_051a9 <= 1000
 PFK_R11 <= 1000
 PFK_R11_reverse_89adc <= 1000
 PFK_R12 <= 1000
 PFK_R12_reverse_a500a <= 1000
 PFK_R13 <= 1000
 PFK_R13_reverse_0e2de <= 1000
 PFK_R20 <= 1000
 PFK_R20_reverse_29211 <= 1000
 PFK_R21 <= 1000
 PFK_R21_reverse_336ca <= 1000
 PFK_R22 <= 1000
 PFK_R22_reverse_37f36 <= 1000
 PFK_R23 <= 1000
 PFK_R23_reverse_e55ae <= 1000
 PFK_R30 <= 1000
 PFK_R30_reverse_fc18f <= 1000
 PFK_R31 <= 1000
 PFK_R31_reverse_3cee8 <= 1000
 PFK_R32 <= 1000
 PFK_R32_reverse_e6e63 <= 1000
 PFK_R33 <= 1000
 PFK_R33_reverse_fbc5d <= 1000
 PFK_R40 <= 1000
 PFK_R40_reverse_48b56 <= 1000
 PFK_R41 <= 1000
 PFK_R41_reverse_20e9f <= 1000
 PFK_R42 <= 1000
 PFK_R42_reverse_3dab0 <= 1000
 PFK_R43 <= 1000
 PFK_R43_reverse_58b16 <= 1000
 PFK_L <= 1000
 PFK_L_reverse_a21e0 <= 1000
 PFK_T1 <= 1000
 PFK_T1_reverse_2ac1a <= 1000
 PFK_T2 <= 1000
 PFK_T2_reverse_4e834 <= 1000
 PFK_T3 <= 1000
 PFK_T3_reverse_96373 <= 1000
 PFK_T4 <= 1000
 PFK_T4_reverse_1d7d4 <= 1000
End
