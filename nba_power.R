#5/20/18 
#nba draft picks (first three seasons in the league)
nba=read.csv("vorpy_sprite.csv")
nba$VORP=as.factor(nba$VORP)
nba$Power=as.factor(nba$Power)

count(power$VORP) #count VORP classes 
median(nba$Weight) #216 lbs average 

#weight histogram 
p=plot_ly(x=nba$Weight,type="histogram")+xlab("Weight")

#VORP (power vs. non-power conference draft picks)
p1=plot_ly(alpha=0.5) %>%
  add_histogram(x=nba$PTS,fill=nba$Power) %>%
  add_histogram(x=nba$PTS,fill=nba$Power) %>%
  layout(barmode="overlay")

power=subset(nba,Power==1)
mean(power$PTS) #13.0
mean(power$PTS) #15.2 

#histogram of points per game (power vs. non-power)
g1=ggplot(nba,alpha=0.6,aes(x=PTS,group=Power,fill=Power))+
  stat_bin(aes(y=..density..),position='dodge')+xlab("Points Per Game")+ggtitle("Non-Power Draft Picks Score More")