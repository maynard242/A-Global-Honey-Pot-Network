import org.apache.spark._
import org.apache.spark.SparkConf

//
// first get the json data from an api call to the mongoDB
//  assumes the file is called "output.json"
//

object Main extends App{

  val rawDF = spark.read.json(sc.wholeTextFiles("output.json").values)

  //
  // the raw DF has a nested structure and all the data is in a single column
  // so explode that column into rows
  
  val exploded = rawDF.select(explode($"data"))

  //
  // now get rid of the superfluous col level of the data 
  //

  val goodDF = exploded.select($"col._id", $"col.destination_ip", $"col.destination_port", $"col.honeypot", $"col.identifier", $"col.protocol", $"col.source_ip", $"col.source_port", $"col.timestamp")

}
