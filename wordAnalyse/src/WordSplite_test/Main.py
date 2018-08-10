#coding=utf-8
import Get_day_data
import Get_keywords
import Get_keynews
import Delete_Repeat
import Get_hot_result
import Global_param
def main():
    for i in range(1,Global_param.number_day):
        Get_day_data.TransforData(i)  #获得当天用户浏览行为
        Get_day_data.TransforDataset(i) #按日期区分新闻
        Get_keywords.Get_keywords(i) #调用jieba获得兴趣度最高的keywords
        Get_keynews.Get_keynews(i) #推荐关键词相关的新闻
    Delete_Repeat.Delete_Repeat() #去除上边结果的重复项
    Get_hot_result.get_hot_result(Global_param.hot_rate) #控制兴趣度，推荐最终结果

main()