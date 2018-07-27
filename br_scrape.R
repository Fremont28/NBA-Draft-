library(rvest)
library(dplyr)
library(purrr)

#scrape 
bball=read_html("https://www.basketball-reference.com/play-index/psl_finder.cgi?request=1&match=single&type=totals&per_minute_base=36&per_poss_base=100&lg_id=NBA&is_playoffs=N&year_min=2004&year_max=2018&franch_id=&season_start=1&season_end=-1&age_min=0&age_max=99&shoot_hand=&height_min=0&height_max=99&birth_country_is=Y&birth_country=&birth_state=&college_id=&draft_year=&is_active=&debut_yr_nba_start=&debut_yr_nba_end=&is_hof=&is_as=&as_comp=gt&as_val=0&award=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&qual=&c1stat=&c1comp=&c1val=&c2stat=&c2comp=&c2val=&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&c5stat=&c5comp=&c6mult=&c6stat=&order_by=vorp&order_by_asc=&offset=7100")

temp71=bball %>%
  html_nodes("table") %>%
  .[[1]] %>% html_table() 

temp71=as.data.frame(temp71)


final_nba=rbind(temp,temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,
                temp9,temp10,temp11,temp12,temp13,temp14,temp15,temp16,
                temp17,temp18,temp19,temp20,temp21,temp22,temp23,
                temp24,temp25,temp26,temp27,temp28,temp29,temp30,
                temp31,temp32,temp33,temp34,temp35,temp36,temp37,
                temp38,temp39,temp40,temp41,temp42,temp43,temp44,
                temp45,temp46,temp47,temp48,temp49,temp50,
                temp51,temp52,temp53,temp54,temp55,temp56,temp57,
                temp58,temp59,temp60,temp61,temp62,temp63,temp64,
                temp65,temp66,temp67,temp68,temp69,temp70)


