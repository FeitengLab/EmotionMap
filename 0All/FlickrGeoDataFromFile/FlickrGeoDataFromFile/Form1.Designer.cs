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
            this.btnImportRegion = new System.Windows.Forms.Button();
            this.btnImportFlickrData = new System.Windows.Forms.Button();
            this.tbxImportRegion = new System.Windows.Forms.TextBox();
            this.tbxImportFlickrDataPath = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.tbxStatus = new System.Windows.Forms.TextBox();
            this.btnOK = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.btnImportSingleFilePath = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.tbxImportSingleFilePath = new System.Windows.Forms.TextBox();
            this.btnExportSingleFilePath = new System.Windows.Forms.Button();
            this.tbxExportSingleFilePath = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.btnOKSingle = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // btnImportRegion
            // 
            this.btnImportRegion.Location = new System.Drawing.Point(433, 72);
            this.btnImportRegion.Name = "btnImportRegion";
            this.btnImportRegion.Size = new System.Drawing.Size(75, 23);
            this.btnImportRegion.TabIndex = 2;
            this.btnImportRegion.Text = "导入";
            this.btnImportRegion.UseVisualStyleBackColor = true;
            this.btnImportRegion.Click += new System.EventHandler(this.btnImportRegion_Click);
            // 
            // btnImportFlickrData
            // 
            this.btnImportFlickrData.Location = new System.Drawing.Point(433, 33);
            this.btnImportFlickrData.Name = "btnImportFlickrData";
            this.btnImportFlickrData.Size = new System.Drawing.Size(75, 23);
            this.btnImportFlickrData.TabIndex = 3;
            this.btnImportFlickrData.Text = "导入";
            this.btnImportFlickrData.UseVisualStyleBackColor = true;
            this.btnImportFlickrData.Click += new System.EventHandler(this.btnImportFlickrData_Click);
            // 
            // tbxImportRegion
            // 
            this.tbxImportRegion.Location = new System.Drawing.Point(138, 74);
            this.tbxImportRegion.Name = "tbxImportRegion";
            this.tbxImportRegion.Size = new System.Drawing.Size(289, 21);
            this.tbxImportRegion.TabIndex = 6;
            // 
            // tbxImportFlickrDataPath
            // 
            this.tbxImportFlickrDataPath.Location = new System.Drawing.Point(138, 33);
            this.tbxImportFlickrDataPath.Name = "tbxImportFlickrDataPath";
            this.tbxImportFlickrDataPath.Size = new System.Drawing.Size(289, 21);
            this.tbxImportFlickrDataPath.TabIndex = 1;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(19, 36);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(113, 12);
            this.label3.TabIndex = 11;
            this.label3.Text = "导入Flickr数据文件";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(19, 77);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(101, 12);
            this.label2.TabIndex = 12;
            this.label2.Text = "导入地点范围文件";
            // 
            // tbxStatus
            // 
            this.tbxStatus.Location = new System.Drawing.Point(6, 130);
            this.tbxStatus.Multiline = true;
            this.tbxStatus.Name = "tbxStatus";
            this.tbxStatus.Size = new System.Drawing.Size(502, 65);
            this.tbxStatus.TabIndex = 13;
            // 
            // btnOK
            // 
            this.btnOK.Location = new System.Drawing.Point(219, 101);
            this.btnOK.Name = "btnOK";
            this.btnOK.Size = new System.Drawing.Size(75, 23);
            this.btnOK.TabIndex = 14;
            this.btnOK.Text = "确定";
            this.btnOK.UseVisualStyleBackColor = true;
            this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.tbxStatus);
            this.groupBox1.Controls.Add(this.btnOK);
            this.groupBox1.Controls.Add(this.btnImportRegion);
            this.groupBox1.Controls.Add(this.btnImportFlickrData);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.tbxImportRegion);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.tbxImportFlickrDataPath);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(515, 207);
            this.groupBox1.TabIndex = 15;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "根据范围筛选点";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.btnOKSingle);
            this.groupBox2.Controls.Add(this.btnExportSingleFilePath);
            this.groupBox2.Controls.Add(this.tbxExportSingleFilePath);
            this.groupBox2.Controls.Add(this.label4);
            this.groupBox2.Controls.Add(this.btnImportSingleFilePath);
            this.groupBox2.Controls.Add(this.tbxImportSingleFilePath);
            this.groupBox2.Controls.Add(this.label1);
            this.groupBox2.Location = new System.Drawing.Point(12, 225);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(515, 123);
            this.groupBox2.TabIndex = 16;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "提取出数值方便计算";
            // 
            // btnImportSingleFilePath
            // 
            this.btnImportSingleFilePath.Location = new System.Drawing.Point(433, 20);
            this.btnImportSingleFilePath.Name = "btnImportSingleFilePath";
            this.btnImportSingleFilePath.Size = new System.Drawing.Size(75, 23);
            this.btnImportSingleFilePath.TabIndex = 16;
            this.btnImportSingleFilePath.Text = "导入";
            this.btnImportSingleFilePath.UseVisualStyleBackColor = true;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(19, 23);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(113, 12);
            this.label1.TabIndex = 17;
            this.label1.Text = "导入Flickr数据文件";
            // 
            // tbxImportSingleFilePath
            // 
            this.tbxImportSingleFilePath.Location = new System.Drawing.Point(138, 20);
            this.tbxImportSingleFilePath.Name = "tbxImportSingleFilePath";
            this.tbxImportSingleFilePath.Size = new System.Drawing.Size(289, 21);
            this.tbxImportSingleFilePath.TabIndex = 15;
            // 
            // btnExportSingleFilePath
            // 
            this.btnExportSingleFilePath.Location = new System.Drawing.Point(433, 60);
            this.btnExportSingleFilePath.Name = "btnExportSingleFilePath";
            this.btnExportSingleFilePath.Size = new System.Drawing.Size(75, 23);
            this.btnExportSingleFilePath.TabIndex = 19;
            this.btnExportSingleFilePath.Text = "导出";
            this.btnExportSingleFilePath.UseVisualStyleBackColor = true;
            // 
            // tbxExportSingleFilePath
            // 
            this.tbxExportSingleFilePath.Location = new System.Drawing.Point(138, 60);
            this.tbxExportSingleFilePath.Name = "tbxExportSingleFilePath";
            this.tbxExportSingleFilePath.Size = new System.Drawing.Size(289, 21);
            this.tbxExportSingleFilePath.TabIndex = 18;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(19, 63);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(113, 12);
            this.label4.TabIndex = 20;
            this.label4.Text = "导出Flickr数据文件";
            // 
            // btnOKSingle
            // 
            this.btnOKSingle.Location = new System.Drawing.Point(219, 87);
            this.btnOKSingle.Name = "btnOKSingle";
            this.btnOKSingle.Size = new System.Drawing.Size(75, 23);
            this.btnOKSingle.TabIndex = 15;
            this.btnOKSingle.Text = "确定";
            this.btnOKSingle.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(538, 353);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnImportRegion;
        private System.Windows.Forms.Button btnImportFlickrData;
        private System.Windows.Forms.TextBox tbxImportRegion;
        private System.Windows.Forms.TextBox tbxImportFlickrDataPath;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox tbxStatus;
        private System.Windows.Forms.Button btnOK;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button btnOKSingle;
        private System.Windows.Forms.Button btnExportSingleFilePath;
        private System.Windows.Forms.TextBox tbxExportSingleFilePath;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button btnImportSingleFilePath;
        private System.Windows.Forms.TextBox tbxImportSingleFilePath;
        private System.Windows.Forms.Label label1;
    }
}

