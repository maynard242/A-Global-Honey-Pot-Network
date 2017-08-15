import org.apache.log4j.{Level, Logger}

import org.apache.spark._
import org.apache.spark.streaming._
import org.apache.spark.streaming.StreamingContext._
import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.spark.SparkConf

object honeypot {
  def main(args: Array[String]) {

if (!Logger.getRootLogger.getAllAppenders.hasMoreElements) {
      Logger.getRootLogger.setLevel(Level.WARN)
    }

val sparkConf = new SparkConf().setAppName("honeypot")

val ssc = new StreamingContext(sparkConf, Seconds(10))
val lines = ssc.socketTextStream("localhost", 6000)

val attacks = lines.map(s => s.split("\\|"))
val countryCount = attacks.map(l => (l(4), 1)).reduceByKeyAndWindow(_ + _, Seconds(10)).transform(_.sortByKey(false))
val cityCount = attacks.map(l => (l(5), 1)).reduceByKeyAndWindow(_ + _, Seconds(10)).transform(_.sortByKey(false))
val portCount = attacks.map(l => (l(2), 1)).reduceByKeyAndWindow(_ + _, Seconds(10)).transform(_.sortByKey(false))
val honeypotCount = attacks.map(l => (l(3), 1)).reduceByKeyAndWindow(_ + _, Seconds(10)).transform(_.sortByKey(false))

countryCount.foreachRDD(rdd => {
      val topList = rdd.take(10)
      println("Attacks info in the last 10 seconds: ")
      println("Country Info #######################################################")
      topList.foreach{case (c , cn) => println("%s attack come from %s".format(cn,c))}
    })

cityCount.foreachRDD(rdd => {
      val topList = rdd.take(10)
      println("City Info #######################################################")
      topList.foreach{case (c , cn) => println("%s attack come from %s".format(cn,c))}
    })

portCount.foreachRDD(rdd => {
      val topList = rdd.take(10)
      println("port Info #######################################################")
      topList.foreach{case (c , cn) => println("%s attack at %s".format(cn,c))}
    })

honeypotCount.foreachRDD(rdd => {
      val topList = rdd.take(10)
      println("Honeypot info #######################################################")
      topList.foreach{case (c , cn) => println("%s attacks are %s".format(cn,c))}
    })

ssc.start()
ssc.awaitTermination()
  }
}
