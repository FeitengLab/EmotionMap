using System;
using System.Collections.Generic;
using System.IO;
using System.Windows.Forms;

/// <Author>
/// Yuhao Kang
/// </Author>
/// <Function>
/// Import Flickr data from all csv files with geotag.
/// Extract points within the selecting boundary.
/// Export the particular points.
/// 打开任意一个Flickr的csv文件。软件将读取文件夹名,在之后的操作中将按照先前的顺序依次遍历所有的csv文件。
/// 打开区域范围的csv文件,获取所有的区域。
/// 依次遍历所有Flickr数据,并与区域范围进行比较,提取出范围内的点并写入csv文件.
/// </Function>
namespace FlickrGeoDataFromFile
{
    public partial class Form1 : Form
    {
        List<Region> regionList = new List<Region>();//所有的矩形区域集合
        string importPath, exportPath, flickrDataFolder, flickrDataCSV, fileType;
        string filenameAll = "faceflickr";

        public Form1()
        {
            InitializeComponent();
        }

        private void btnImportFlickrData_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.CheckFileExists = true;
            openFileDialog.Title = "打开数据";
            openFileDialog.Filter = "所有文件(*.*)|*.*";
            openFileDialog.Multiselect = false;
            openFileDialog.RestoreDirectory = true;
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    //获取Flickr数据文件路径
                    flickrDataFolder = openFileDialog.FileName.Substring(0, openFileDialog.FileName.LastIndexOf('\\'));

                    fileType = openFileDialog.FileName.Split('.')[1];
                    flickrDataCSV = string.Format("{0}\\{1}0.{2}", flickrDataFolder, filenameAll, fileType);
                    tbxImportFlickrDataPath.Text = flickrDataCSV;
                }
                catch (Exception ex)
                {
                    ErrorSolve(ex);
                }
            }
        }

        private void btnImportRegion_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.CheckFileExists = true;
            openFileDialog.Title = "打开区域文件";
            openFileDialog.Filter = "所有文件(*.*)|*.*";
            openFileDialog.Multiselect = false;
            openFileDialog.RestoreDirectory = true;
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    using (StreamReader streamReader = new StreamReader(openFileDialog.FileName))
                    {
                        //获取区域表详细信息
                        string line = streamReader.ReadLine();
                        while (line != null)
                        {
                            Region region = new Region(Convert.ToDouble(line.Split(',')[0]), Convert.ToDouble(line.Split(',')[1]), Convert.ToDouble(line.Split(',')[2]), Convert.ToDouble(line.Split(',')[3]), line.Split(',')[4]);
                            region.CreateStreamWriter(String.Format("{0}\\{1}.csv", flickrDataFolder, region.name));
                            regionList.Add(region);
                            line = streamReader.ReadLine();
                        }
                        tbxImportRegion.Text = openFileDialog.FileName;
                    }
                    tbxStatus.Text += "导入区域情况完毕!\n";
                }
                catch (Exception ex)
                {
                    ErrorSolve(ex);
                }
            }
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            //读取所有的Flickr数据
            for (int i = 0; i <= 25; i++)
            {
                try
                {
                    flickrDataCSV = string.Format("{0}\\{1}{2}.{3}", flickrDataFolder, filenameAll, i, fileType);
                    ExtractPts(new StreamReader(flickrDataCSV));
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.ToString());
                }
            }
            tbxStatus.Text += "导出完毕!";
        }

        /// <summary>
        /// 获取在区域范围内的点
        /// </summary>
        /// <param name="streamWriter"></param>
        private void ExtractPts(StreamReader streamReader)
        {
            try
            {
                //读取Flickr数据
                string flickrDataLine = streamReader.ReadLine();
                while (flickrDataLine != null)
                {
                    //读取一行Flickr数据并进行处理
                    FlickrData flickrData = new FlickrData(flickrDataLine);
                    foreach (Region region in regionList)
                    {
                        //判断是否在区域内
                        if (region.IsInBoundary(flickrData.longitude, flickrData.latitude))
                        {
                            //如果在区域内则写入文件
                            region.WritePts(flickrData);
                        }
                    }
                    flickrDataLine = streamReader.ReadLine();
                }
                streamReader.Close();
            }
            catch (Exception ex)
            {
                ErrorSolve(ex);
            }
        }

        /// <summary>
        /// 处理错误信息
        /// </summary>
        /// <param name="ex"></param>
        public void ErrorSolve(Exception ex)
        {
            //MessageBox.Show(ex.ToString());
            using (StreamWriter sw = new StreamWriter(String.Format("{0}\\log.txt", flickrDataFolder)))
            {
                sw.WriteLine(String.Format("{0}:{1}\n", DateTime.Now.ToString(), ex.ToString()));
            }
        }

        /// <summary>
        /// 从数据表中读取出Flickr数据
        /// </summary>
        public class FlickrData
        {
            long photoId, photoUploadTime;
            string userid, photoTakeTime, photoTitle, photoDescription, photoGeotag, url;
            public double longitude { get; }
            public double latitude { get; }
            public double happiness { get; }
            public double neutral { get; }
            public double sadness { get; }
            public double disgust { get; }
            public double anger { get; }
            public double fear { get; }
            public double surprise { get; }
            public double facequality_s { get; }
            public double facequality_v { get; }
            public double smile_s { get; }
            public double smile_v { get; }
            public double gender { get; }
            public double ethnicity { get; }
            public double age { get; }
            int accuracy, facenum;
            string flickrDataLine;

            public FlickrData(string flickrDataLine)
            {
                this.flickrDataLine = flickrDataLine;
                
                int i = 0;
                //从文件中读取出Flickr数据并分配给相应的对象
                photoId = Convert.ToInt64(flickrDataLine.Split('\t')[i++]);
                userid = Convert.ToString(flickrDataLine.Split('\t')[i++]);
                photoTakeTime = Convert.ToString(flickrDataLine.Split('\t')[i++]);
                photoUploadTime = Convert.ToInt64(flickrDataLine.Split('\t')[i++]);
                photoTitle = Convert.ToString(flickrDataLine.Split('\t')[i++]);
                photoDescription = Convert.ToString(flickrDataLine.Split('\t')[i++]);
                photoGeotag = Convert.ToString(flickrDataLine.Split('\t')[i++]);
                longitude = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                latitude = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                accuracy = Convert.ToInt32(flickrDataLine.Split('\t')[i++]);
                url = Convert.ToString(flickrDataLine.Split('\t')[i++]);
                ///*
                facenum = Convert.ToInt32(flickrDataLine.Split('\t')[i++]);
                // 按照'happiness', 'neutral', 'sadness', 'disgust', 'anger', 'fear', 'surprise' 的顺序添加情绪指数
                happiness = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                neutral = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                sadness = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                disgust = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                anger = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                fear = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                surprise = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                // facequality, smile, gender, ethnicity, age
                facequality_s = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                facequality_v = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                smile_s = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                smile_v = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                gender = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                ethnicity = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                age = Convert.ToDouble(flickrDataLine.Split('\t')[i++]);
                //*/
            }
            public string FlickrDataWrite()
            {
                return flickrDataLine;
            }
        }

        /// <summary>
        /// 从区域表中读取出各个区域的情况
        /// </summary>
        public class Region
        {
            public double maxLon { get; }
            public double maxLat { get; }
            public double minLon { get; }
            public double minLat { get; }
            public string name { get; }
            private StreamWriter streamWriter;

            public Region(double maxLat, double minLon, double minLat, double maxLon, string name)
            {
                this.maxLat = maxLat;
                this.minLon = minLon;
                this.minLat = minLat;
                this.maxLon = maxLon;
                this.name = name;
            }

            /// <summary>
            /// 创建写入流
            /// </summary>
            /// <param name="path"></param>
            public void CreateStreamWriter(string path)
            {
                streamWriter = new StreamWriter(path);
            }

            /// <summary>
            /// 判断是否在区域内,如果传入的点在区域内,则返回True,否则返回False
            /// </summary>
            /// <param name="lon"></param>
            /// <param name="lat"></param>
            /// <returns></returns>
            public bool IsInBoundary(double lon, double lat)
            {
                if (lon >= minLon && lon <= maxLon)
                {
                    if (lat >= minLat && lat <= maxLat)
                    {
                        return true;
                    }
                }
                return false;
            }

            /// <summary>
            /// 写入文件
            /// </summary>
            /// <param name="flickrData"></param>
            /// <returns></returns>
            public bool WritePts(FlickrData flickrData)
            {
                try
                {
                    streamWriter.WriteLine(flickrData.FlickrDataWrite());
                    return true;
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.ToString());
                    return false;
                }
            }
        }
    }
}
