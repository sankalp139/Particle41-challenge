output "alb_dns_name" {
  description = "Public ALB DNS name"
  value       = aws_lb.app.dns_name
}
