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
            this.SuspendLayout();
            // 
            // btnImportRegion
            // 
            this.btnImportRegion.Location = new System.Drawing.Point(439, 60);
            this.btnImportRegion.Name = "btnImportRegion";
            this.btnImportRegion.Size = new System.Drawing.Size(75, 23);
            this.btnImportRegion.TabIndex = 2;
            this.btnImportRegion.Text = "导入";
            this.btnImportRegion.UseVisualStyleBackColor = true;
            this.btnImportRegion.Click += new System.EventHandler(this.btnImportRegion_Click);
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
            // tbxImportRegion
            // 
            this.tbxImportRegion.Location = new System.Drawing.Point(144, 62);
            this.tbxImportRegion.Name = "tbxImportRegion";
            this.tbxImportRegion.Size = new System.Drawing.Size(289, 21);
            this.tbxImportRegion.TabIndex = 6;
            // 
            // tbxImportFlickrDataPath
            // 
            this.tbxImportFlickrDataPath.Location = new System.Drawing.Point(144, 21);
            this.tbxImportFlickrDataPath.Name = "tbxImportFlickrDataPath";
            this.tbxImportFlickrDataPath.Size = new System.Drawing.Size(289, 21);
            this.tbxImportFlickrDataPath.TabIndex = 1;
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
            this.label2.Location = new System.Drawing.Point(25, 65);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(101, 12);
            this.label2.TabIndex = 12;
            this.label2.Text = "导入地点范围文件";
            // 
            // tbxStatus
            // 
            this.tbxStatus.Location = new System.Drawing.Point(12, 118);
            this.tbxStatus.Multiline = true;
            this.tbxStatus.Name = "tbxStatus";
            this.tbxStatus.Size = new System.Drawing.Size(502, 65);
            this.tbxStatus.TabIndex = 13;
            // 
            // btnOK
            // 
            this.btnOK.Location = new System.Drawing.Point(225, 89);
            this.btnOK.Name = "btnOK";
            this.btnOK.Size = new System.Drawing.Size(75, 23);
            this.btnOK.TabIndex = 14;
            this.btnOK.Text = "确定";
            this.btnOK.UseVisualStyleBackColor = true;
            this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(526, 195);
            this.Controls.Add(this.btnOK);
            this.Controls.Add(this.tbxStatus);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.tbxImportFlickrDataPath);
            this.Controls.Add(this.tbxImportRegion);
            this.Controls.Add(this.btnImportFlickrData);
            this.Controls.Add(this.btnImportRegion);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

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
    }
}

