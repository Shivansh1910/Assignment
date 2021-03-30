import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { UploadService } from './upload.service';

@Component({
  selector: 'app-certificate',
  templateUrl: './certificate.component.html',
  styleUrls: ['./certificate.component.scss']
})
export class CertificateComponent implements OnInit {
  isCollapsed = true;
  focus;
  focus1;
  focus2;


  DJANGO_SERVER = 'http://127.0.0.1:8000'
  form: FormGroup;
  response;
  imageURL;
  name;
  x;
  y;
  begin;
  discript;
  discript1;
  discript2;

  constructor(private formBuilder: FormBuilder, private uploadService: UploadService, private http: HttpClient, private router: Router) { }

  ngOnInit() {
    var header = new HttpHeaders({
      "Authorization": "Token " + localStorage.getItem('cp_token')
    })
    this.form = this.formBuilder.group({
      profile: ['']
    });
  }

  onNameChange(event) {
    this.name = event.target.value;
  }

  onXChange(event) {
    this.x = event.target.value;
  }

  onYChange(event) {
    this.y = event.target.value;
  }

  onBeginChange(event) {
    this.begin = event.target.value;
  }

  onDiscChange(event) {
    this.discript = event.target.value;
  }

  onDisc1Change(event) {
    this.discript1 = event.target.value;
  }

  onDiscbChange(event) {
    this.discript2 = event.target.value;
  }

  onChange(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.form.get('profile').setValue(file);
    }
  }

  onSubmit() {
    const formData = new FormData();
    formData.append('file', this.form.get('profile').value);
    formData.append('x', this.x)
    formData.append('y', this.y)
    formData.append('certificate_name', this.name)
    formData.append('is_discription', "false")
    formData.append('discription', this.discript)


    this.uploadService.upload(formData).subscribe(
      (res) => {
        this.response = res;
        this.imageURL = `${this.DJANGO_SERVER}${res.file}`;
        console.log(res);
        console.log(this.imageURL);
      },
      (err) => {
        console.log(err);
      }
    );
  }

  onSubmitd() {
    const formData = new FormData();
    formData.append('file', this.form.get('profile').value);
    formData.append('x', this.x)
    formData.append('y', this.y)
    formData.append('certificate_name', this.name)
    formData.append('is_discription', "true")
    formData.append('begin', this.begin)
    formData.append('discription', this.discript)
    formData.append('discription1', this.discript1)
    formData.append('discription2', this.discript2)

    this.uploadService.upload(formData).subscribe(
      (res) => {
        this.response = res;
        this.imageURL = `${this.DJANGO_SERVER}${res.file}`;
        console.log(res);
        console.log(this.imageURL);
      },
      (err) => {
        console.log(err);
      }
    );
  }

  checkit() {
    var url = "http://127.0.0.1:8000/portal/generate/";

    var body = new FormData()
    body.append('event', this.name)
    body.append('action', "generate")

    var header = new HttpHeaders({
      "Authorization": "Token " + localStorage.getItem('cp_token')
    })

    this.http.post<any>(url, body, { headers: header }).subscribe(
      data => {
        console.log(data)
        window.open(data);
      }
    )

  }
  logout() {
    localStorage.removeItem('cp_token')
    this.router.navigateByUrl('/log')
  }

}
