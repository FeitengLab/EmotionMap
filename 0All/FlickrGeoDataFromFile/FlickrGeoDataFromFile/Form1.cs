using System;
using System.IO;
using System.Threading;
using System.Windows.Forms;

/// <Author>
/// Yuhao Kang
/// </Author>
/// <Function>
/// Import Flickr data from all csv files with geotag.
/// Extract points within the selecting boundary.
/// Export the particular points.
/// 打开任意一个Flickr的csv文件。软件将读取文件夹名,之后按照先前的顺序依次遍历所有的csv文件。
/// 根据输入的几何范围,搜索所有范围内的点并提取出来,再写入csv文件。
/// 文件名需手动输入。
/// </Function>
namespace FlickrGeoDataFromFile
{
    public partial class Form1 : Form
    {
        double maxLat, maxLon, minLat, minLon;
        string importPath, exportPath, flickrDataFolder, flickrDataCSV;

        public Form1()
        {
            InitializeComponent();
        }

        private void btnImportFlickrData_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.CheckFileExists = true;
            openFileDialog.Title = "打开CSV";
            openFileDialog.Filter = "CSV(*.csv)|*.csv;|所有文件(*.*)|*.*";
            openFileDialog.Multiselect = false;
            openFileDialog.RestoreDirectory = true;
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    //获取Flickr数据文件路径
                    flickrDataFolder = openFileDialog.FileName.Substring(0, openFileDialog.FileName.LastIndexOf('\\'));
                    flickrDataCSV = string.Format("{0}\\yfcc100m_dataset-0-x.csv", flickrDataFolder);
                    tbxImportFlickrDataPath.Text = flickrDataCSV;
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.ToString());
                }
            }
        }

        private void btnExportFlickrData_Click(object sender, EventArgs e)
        {
            tbxStatus.Text = "";
            //地理范围
            maxLat = Convert.ToDouble(tbxMaxLat.Text);
            minLat = Convert.ToDouble(tbxMinLat.Text);
            maxLon = Convert.ToDouble(tbxMaxLon.Text);
            minLon = Convert.ToDouble(tbxMinLon.Text);
            //导出文件
            exportPath = string.Format("{0}\\{1}.csv", flickrDataFolder, tbxExportFlickrDataName.Text);

            using (StreamWriter flickrStreamWriter = new StreamWriter(exportPath))
            {
                for (int i = 0; i < 2; i++)
                {
                    if (i <= 5)
                    {
                        flickrDataCSV = string.Format("{0}\\yfcc100m_dataset-{1}-x.csv", flickrDataFolder, i);
                        tbxStatus.Text += string.Format("开始读取文件:{0}", flickrDataCSV);
                        ExtractPtsInBoundary(flickrStreamWriter);
                    }
                    else
                    {
                        for (int j = 0; j < 5; j++)
                        {
                            flickrDataCSV = string.Format("{0}\\yfcc100m_dataset-{1}-x-{2}.csv", flickrDataFolder, i, j);
                            tbxStatus.Text += string.Format("开始读取文件:{0}", flickrDataCSV);
                            ExtractPtsInBoundary(flickrStreamWriter);
                        }
                    }
                }
            }
            tbxStatus.Text += "导出完毕!";
        }

        /// <summary>
        /// 获取在区域范围内的点
        /// </summary>
        /// <param name="streamWriter"></param>
        private void ExtractPtsInBoundary(StreamWriter streamWriter)
        {
            using (StreamReader flickrStreamReader = new StreamReader(flickrDataCSV))
            {
                string flickrDataLine = flickrStreamReader.ReadLine();
                while (flickrDataLine != null)
                {
                    FlickrData flickrData = new FlickrData(flickrDataLine);
                    if (IsInBoundary(flickrData.longitude, flickrData.latitude))
                    {
                        //如果点在范围内则写入文件
                        streamWriter.WriteLine(flickrData.FlickrDataWrite());
                    }
                    flickrDataLine = flickrStreamReader.ReadLine();
                }
            }
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
    }
    public class FlickrData
    {
        long photoId, photoUploadTime;
        string userid, photoTakeTime, photoTitle, photoDescription, photoGeotag, url;
        public double longitude { get; }
        public double latitude { get; }
        int accuracy;
        string flickrDataLine;

        public FlickrData(string flickrDataLine)
        {
            this.flickrDataLine = flickrDataLine;
            //从文件中读取出Flickr数据并分配给相应的对象
            photoId = Convert.ToInt64(flickrDataLine.Split('\t')[0]);
            userid = Convert.ToString(flickrDataLine.Split('\t')[1]);
            photoTakeTime = Convert.ToString(flickrDataLine.Split('\t')[2]);
            photoUploadTime = Convert.ToInt64(flickrDataLine.Split('\t')[3]);
            photoTitle = Convert.ToString(flickrDataLine.Split('\t')[4]);
            photoDescription = Convert.ToString(flickrDataLine.Split('\t')[5]);
            photoGeotag = Convert.ToString(flickrDataLine.Split('\t')[6]);
            longitude = Convert.ToDouble(flickrDataLine.Split('\t')[7]);
            latitude = Convert.ToDouble(flickrDataLine.Split('\t')[8]);
            accuracy = Convert.ToInt32(flickrDataLine.Split('\t')[9]);
            url = Convert.ToString(flickrDataLine.Split('\t')[10]);
        }
        public string FlickrDataWrite()
        {
            return flickrDataLine;
        }
    }
}
