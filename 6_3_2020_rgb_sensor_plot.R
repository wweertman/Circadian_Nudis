setwd("~/R/Theresa_FHL/CODE")
library(lubridate)

dat <- read.csv('../DATA/6_3_2020_light_test/DATALOG.TXT')

dates <- dat$date
date_list <- 1:nrow(dat)
time_list <- 1:nrow(dat)

less_than_2 <- function(a_character){
  if (nchar(a_character) < 2){
    a_character <- paste0('0', a_character)
  }
  return(a_character)
}

n <- 0
for (d in dates){
  
  n <- n + 1
  
  date_split <- unlist(strsplit(d,'/'))
  
  month_hold <- less_than_2(date_split[1])
  day_hold <- less_than_2(date_split[2])
  year_hold <- less_than_2(date_split[3])
  
  date_list[n] <- paste0(year_hold,
                         '-',
                         month_hold,
                         '-',
                         day_hold)
  
  
  time_split <- unlist(strsplit(as.character(dat$hh.mm.ss)[n],':'))
  
  hour_hold <- less_than_2(time_split[1])
  minute_hold <- less_than_2(time_split[2])
  second_hold <- less_than_2(time_split[3])
  
  time_list[n] <- paste0(hour_hold,
                        ':',
                        minute_hold,
                        ':',
                        second_hold)
  
}


dat$date <- date_list
dat$hh.mm.ss <- time_list

dat$date_time <- paste(dat$date,dat$hh.mm.ss)
dat$date_time <- as.POSIXct(dat$date_time,
                            format = '%Y-%m-%d %H:%M:%S')

plot(lux ~ date_time,
     data = dat,
     type = 'l',
     ylim = c(0,2000))

points(red ~ date_time,
       data = dat,
       type = 'l',
       col = 'red')
points(blue ~ date_time,
       data = dat,
       type = 'l',
       col = 'blue')
points(green ~ date_time,
       data = dat,
       type = 'l',
       col = 'green')
