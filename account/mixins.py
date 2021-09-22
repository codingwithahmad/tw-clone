
class FormValid():
	

	def form_valid(self, form):
		self.obj = form.save(commit=False)
		self.obj.author = self.request.user


		return super().form_valid(form)