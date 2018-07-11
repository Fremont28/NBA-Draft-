#7/11/18 
#energy states (based on velocity and slope) 
class High_Energy_State():
    def __init__(self):
        pass
    
    #how frequently rider acheives a high energy state on the uphill? 
    def velocity_score_uphill(self,grade,velocity):
        pos_high_velo=[]
        pos_avg_velo=[]
        pos_velo_low=[]
        #slope percentiles 
        df_slope=grade 
        df_slope=np.asarray(df_slope)
        df_slope_high=np.percentile(df_slope,80)
        df_slope_avg=np.percentile(df_slope,50)
        df_slope=np.asarray(df_slope)
        df_slope=df_slope.tolist()
        #velocity percentiles
        df_velo=velocity
        df_velo=np.asarray(df_velo)
        df_velo_high=np.percentile(df_velo,85)
        df_velo_high1=np.percentile(df_velo,70)
        df_velo_avg=np.percentile(df_velo,50)
        df_velo=np.asarray(df_velo)
        df_velo=df_velo.tolist() 
        for i in range(0,len(df_slope)):
            slope=df_slope[i]
            velocity=df_velo[i]
            if (slope>=df_slope_high and velocity>=df_velo_avg):
                pos_high_velo.append(velocity)
            if (slope>=df_slope_avg and slope<df_slope_high) and (velocity>=df_velo_high1): 
                pos_avg_velo.append(velocity)
            if (slope<df_slope_avg and velocity>df_velo_high):
                pos_velo_low.append(velocity)
        high_energy_count=len(pos_high_velo)+len(pos_avg_velo)+len(pos_velo_low)
        total_count=len(df_velo)
        return high_energy_count/total_count

    def velocity_score_downhill(self,grade,velocity):
        neg_high_velo=[]
        neg_avg_velo=[]
        neg_velo_low=[]
        #slope percentiles 
        df_slope=grade 
        df_slope=np.asarray(df_slope)
        df_slope_high=np.percentile(df_slope,80)
        df_slope_avg=np.percentile(df_slope,50)
        df_slope=np.asarray(df_slope)
        df_slope=df_slope.tolist()
        #velocity percentiles
        df_velo=velocity
        df_velo=np.asarray(df_velo)
        df_velo_high=np.percentile(df_velo,85)
        df_velo_high1=np.percentile(df_velo,70)
        df_velo_avg=np.percentile(df_velo,50)
        df_velo=np.asarray(df_velo)
        df_velo=df_velo.tolist() 
        for i in range(0,len(df_slope)):
            slope=df_slope[i]
            velocity=df_velo[i]
            if (slope>=df_slope_high and velocity>=df_velo_avg):
                neg_high_velo.append(velocity)
            if (slope>=df_slope_avg and slope<df_slope_high) and (velocity>=df_velo_high1): 
                neg_avg_velo.append(velocity)
            if (slope<df_slope_avg and velocity>df_velo_high):
                neg_velo_low.append(velocity)
        high_energy_count=len(neg_high_velo)+len(neg_avg_velo)+len(neg_velo_low)
        total_count=len(df_velo)
        return high_energy_count/total_count

energy_state=High_Energy_State()
energy_state.velocity_score_uphill(pos_grade_list,pos_velo_list)
energy_state.velocity_score_downhill(neg_grade_list,neg_velo_list)