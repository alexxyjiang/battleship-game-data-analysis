#!/usr/bin/R
model_data  <- read.table("./data/allbuild.data",   head=T)
lm_cv       <- lm(CV ~ Fuel + Ammo + Fe + Al,       data=model_data)
lm_cv
lm_cvl      <- lm(CVL ~ Fuel + Ammo + Fe + Al,       data=model_data)
lm_cvl
lm_cvs      <- lm(CVS ~ Fuel + Ammo + Fe + Al,       data=model_data)
lm_cvs
lm_bb       <- lm(BB ~ Fuel + Ammo + Fe + Al,       data=model_data)
lm_bb
lm_bc       <- lm(BC ~ Fuel + Ammo + Fe + Al,       data=model_data)
lm_bc
lm_ca       <- lm(CA ~ Fuel + Ammo + Fe + Al,       data=model_data)
lm_ca
lm_cl       <- lm(CL ~ Fuel + Ammo + Fe + Al,       data=model_data)
lm_cl
lm_dd       <- lm(DD ~ Fuel + Ammo + Fe + Al,       data=model_data)
lm_dd
lm_bm       <- lm(BM ~ Fuel + Ammo + Fe + Al,       data=model_data)
lm_bm
lm_ss       <- lm(SS ~ Fuel + Ammo + Fe + Al,       data=model_data)
lm_ss
