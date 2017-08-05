namespace FlickrGeoDataFromFile
{
    partial class Form1
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.btnExportFlickrData = new System.Windows.Forms.Button();
            this.btnImportFlickrData = new System.Windows.Forms.Button();
            this.tbxExportFlickrDataName = new System.Windows.Forms.TextBox();
            this.tbxMaxLat = new System.Windows.Forms.TextBox();
            this.tbxMinLat = new System.Windows.Forms.TextBox();
            this.tbxMaxLon = new System.Windows.Forms.TextBox();
            this.tbxMinLon = new System.Windows.Forms.TextBox();
            this.tbxImportFlickrDataPath = new System.Windows.Forms.TextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label5 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.tbxStatus = new System.Windows.Forms.TextBox();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // btnExportFlickrData
            // 
            this.btnExportFlickrData.Location = new System.Drawing.Point(439, 288);
            this.btnExportFlickrData.Name = "btnExportFlickrData";
            this.btnExportFlickrData.Size = new System.Drawing.Size(75, 23);
            this.btnExportFlickrData.TabIndex = 2;
            this.btnExportFlickrData.Text = "导出";
            this.btnExportFlickrData.UseVisualStyleBackColor = true;
            this.btnExportFlickrData.Click += new System.EventHandler(this.btnExportFlickrData_Click);
            // 
            // btnImportFlickrData
            // 
            this.btnImportFlickrData.Location = new System.Drawing.Point(439, 21);
            this.btnImportFlickrData.Name = "btnImportFlickrData";
            this.btnImportFlickrData.Size = new System.Drawing.Size(75, 23);
            this.btnImportFlickrData.TabIndex = 3;
            this.btnImportFlickrData.Text = "导入";
            this.btnImportFlickrData.UseVisualStyleBackColor = true;
            this.btnImportFlickrData.Click += new System.EventHandler(this.btnImportFlickrData_Click);
            // 
            // tbxExportFlickrDataName
            // 
            this.tbxExportFlickrDataName.Location = new System.Drawing.Point(144, 290);
            this.tbxExportFlickrDataName.Name = "tbxExportFlickrDataName";
            this.tbxExportFlickrDataName.Size = new System.Drawing.Size(289, 21);
            this.tbxExportFlickrDataName.TabIndex = 6;
            // 
            // tbxMaxLat
            // 
            this.tbxMaxLat.Location = new System.Drawing.Point(15, 35);
            this.tbxMaxLat.Name = "tbxMaxLat";
            this.tbxMaxLat.Size = new System.Drawing.Size(100, 21);
            this.tbxMaxLat.TabIndex = 2;
            // 
            // tbxMinLat
            // 
            this.tbxMinLat.Location = new System.Drawing.Point(270, 188);
            this.tbxMinLat.Name = "tbxMinLat";
            this.tbxMinLat.Size = new System.Drawing.Size(100, 21);
            this.tbxMinLat.TabIndex = 4;
            // 
            // tbxMaxLon
            // 
            this.tbxMaxLon.Location = new System.Drawing.Point(376, 188);
            this.tbxMaxLon.Name = "tbxMaxLon";
            this.tbxMaxLon.Size = new System.Drawing.Size(100, 21);
            this.tbxMaxLon.TabIndex = 5;
            // 
            // tbxMinLon
            // 
            this.tbxMinLon.Location = new System.Drawing.Point(121, 35);
            this.tbxMinLon.Name = "tbxMinLon";
            this.tbxMinLon.Size = new System.Drawing.Size(100, 21);
            this.tbxMinLon.TabIndex = 3;
            // 
            // tbxImportFlickrDataPath
            // 
            this.tbxImportFlickrDataPath.Location = new System.Drawing.Point(144, 21);
            this.tbxImportFlickrDataPath.Name = "tbxImportFlickrDataPath";
            this.tbxImportFlickrDataPath.Size = new System.Drawing.Size(289, 21);
            this.tbxImportFlickrDataPath.TabIndex = 1;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.label);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.tbxMaxLat);
            this.groupBox1.Controls.Add(this.tbxMinLon);
            this.groupBox1.Controls.Add(this.tbxMinLat);
            this.groupBox1.Controls.Add(this.tbxMaxLon);
            this.groupBox1.Location = new System.Drawing.Point(12, 50);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(502, 215);
            this.groupBox1.TabIndex = 10;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "地理方位";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(394, 164);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(59, 12);
            this.label5.TabIndex = 12;
            this.label5.Text = "longitude";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(288, 164);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(53, 12);
            this.label4.TabIndex = 11;
            this.label4.Text = "latitude";
            // 
            // label
            // 
            this.label.AutoSize = true;
            this.label.Location = new System.Drawing.Point(140, 74);
            this.label.Name = "label";
            this.label.Size = new System.Drawing.Size(59, 12);
            this.label.TabIndex = 10;
            this.label.Text = "longitude";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(31, 74);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 12);
            this.label1.TabIndex = 9;
            this.label1.Text = "latitude";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(25, 24);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(113, 12);
            this.label3.TabIndex = 11;
            this.label3.Text = "导入Flickr数据文件";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(25, 293);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(101, 12);
            this.label2.TabIndex = 12;
            this.label2.Text = "导出Flickr文件名";
            // 
            // tbxStatus
            // 
            this.tbxStatus.Location = new System.Drawing.Point(12, 320);
            this.tbxStatus.Multiline = true;
            this.tbxStatus.Name = "tbxStatus";
            this.tbxStatus.Size = new System.Drawing.Size(502, 65);
            this.tbxStatus.TabIndex = 13;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(526, 397);
            this.Controls.Add(this.tbxStatus);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.tbxImportFlickrDataPath);
            this.Controls.Add(this.tbxExportFlickrDataName);
            this.Controls.Add(this.btnImportFlickrData);
            this.Controls.Add(this.btnExportFlickrData);
            this.Name = "Form1";
            this.Text = "Form1";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnExportFlickrData;
        private System.Windows.Forms.Button btnImportFlickrData;
        private System.Windows.Forms.TextBox tbxExportFlickrDataName;
        private System.Windows.Forms.TextBox tbxMaxLat;
        private System.Windows.Forms.TextBox tbxMinLat;
        private System.Windows.Forms.TextBox tbxMaxLon;
        private System.Windows.Forms.TextBox tbxMinLon;
        private System.Windows.Forms.TextBox tbxImportFlickrDataPath;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox tbxStatus;
    }
}

