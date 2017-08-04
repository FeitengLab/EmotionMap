using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
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
                    flickrDataFolder = openFileDialog.FileName.Substring(0, openFileDialog.FileName.LastIndexOf('\\'));
                    flickrDataCSV = string.Format("{0}\\yfcc100m_dataset-0-x.csv", flickrDataFolder);
                    MessageBox.Show(flickrDataCSV);
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.ToString());
                }
            }
        }

        private void btnExportFlickrData_Click(object sender, EventArgs e)
        {
            maxLat = Convert.ToDouble(tbxMaxLat.Text);
            minLat = Convert.ToDouble(tbxMinLat.Text);
            maxLon = Convert.ToDouble(tbxMaxLon.Text);
            minLon = Convert.ToDouble(tbxMinLon.Text);
            importPath = tbxImportFlickrDataPath.Text;
            exportPath = tbxExportFlickrDataPath.Text;
        }
    }
    public class FlickrData
    {
        long photoId, photoUploadTime;
        string userid, photoTakeTime, photoTitle, photoDescription, photoGeotag, url;
        int longitude, latitude, accuracy;
        public string FlickrDataWrite()
        {
            return String.Format("{0}", photoId);
        }
    }
}
