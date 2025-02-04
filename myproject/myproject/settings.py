#The numeric value (here 300) sets the order in which pipelines are run. Lower numbers run earlier. For a simple setup, any value works as long as it's the only pipeline.

ITEM_PIPELINES = {
    'myproject.pipelines.PostgresPipeline': 300,
}

SPIDER_MODULES = ['myproject.spiders']





